import glob
import os
import shutil
import sys
import tempfile

import yt_dlp

CHOCO_FFMPEG = r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

COOKIE_BROWSERS = ("chrome", "edge", "firefox")

# Where downloaded videos are saved
DEFAULT_OUTPUT_DIR = r"C:\Users\SERVER\Downloads"


def find_ffmpeg():
    """Return an ffmpeg path yt-dlp can use, or None."""
    found = shutil.which("ffmpeg")
    if found:
        return found
    if os.path.isfile(CHOCO_FFMPEG):
        return CHOCO_FFMPEG
    return None


def base_opts(ffmpeg_path, output_dir):
    return {
        'format': 'bv*+ba/b',
        'outtmpl': f'{output_dir}/%(uploader,uploader_id)s_%(title).100s_%(id)s.%(ext)s',
        'noplaylist': True,
        'socket_timeout': 30,
        'retries': 10,
        'fragment_retries': 10,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        },
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'ffmpeg_location': ffmpeg_path,
    }


def is_network_error(msg):
    return "Failed to connect" in msg or "Could not connect" in msg


def report_error(msg):
    if is_network_error(msg):
        print("\n\u274c Network error \u2014 couldn't reach the site's servers.")
        print("This isn't a code bug. Check your connection/VPN and try again.")
    elif any(code in msg for code in ("401", "403", "429", "rate-limit", "rate limit")):
        print("\n\U0001f512 Instagram refused the request (login required / rate limited).")
        print("Log into instagram.com in Chrome/Edge/Firefox, then run this script again \u2014")
        print("it will reuse your browser cookies automatically.")
    elif "ffmpeg" in msg.lower():
        print("\n\u274c ffmpeg problem: ffmpeg is installed but yt-dlp couldn't use it.")
        print("Try running again, or re-install it: choco install ffmpeg")
    else:
        print(f"\n\u274c Download error: {msg}")


class _QuietLogger:
    """Swallows yt-dlp's cookie-extraction chatter."""

    def debug(self, *args, **kwargs):
        pass

    info = warning = error = debug


def _cookie_db_exists(browser):
    """Cheap check: does this browser have a cookie database on disk at all?"""
    home = os.path.expanduser("~")
    local = os.path.join(home, "AppData", "Local")
    roaming = os.path.join(home, "AppData", "Roaming")
    if browser == "chrome":
        return os.path.isfile(os.path.join(
            local, "Google", "Chrome", "User Data", "Default", "Network", "Cookies"))
    if browser == "edge":
        return os.path.isfile(os.path.join(
            local, "Microsoft", "Edge", "User Data", "Default", "Network", "Cookies"))
    if browser == "firefox":
        profiles = os.path.join(roaming, "Mozilla", "Firefox", "Profiles")
        return any(
            os.path.isfile(os.path.join(profile, "cookies.sqlite"))
            for profile in glob.glob(os.path.join(profiles, "*"))
        )
    return False


def detect_browser_cookies():
    """Quietly find a browser whose cookies yt-dlp can actually load, or None."""
    import yt_dlp.cookies as cookies_mod

    for browser in COOKIE_BROWSERS:
        if not _cookie_db_exists(browser):
            continue  # browser not installed / never used -> don't even try
        try:
            jar = cookies_mod.extract_cookies_from_browser(browser, logger=_QuietLogger())
            if any(True for _ in jar):
                return browser
        except Exception:
            continue  # e.g. Edge DPAPI decryption failure (yt-dlp #10927)
    return None


def download(url, output_dir=DEFAULT_OUTPUT_DIR):
    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        print("\n\u274c ffmpeg not found. Install it with: choco install ffmpeg")
        return

    print(f"\U0001f3ac Using ffmpeg: {ffmpeg_path}")

    tmp_dirs = []
    last_error = None
    info = None
    try:
        # Reuse browser cookies when possible (bypasses Instagram login walls),
        # then fall back to a plain anonymous download.
        cookie_browser = detect_browser_cookies()
        if cookie_browser:
            print(f"\U0001f36a Using cookies from {cookie_browser} (helps with Instagram login walls)")
            attempts = (cookie_browser, None)
        else:
            print("\u26a0\ufe0f  No usable browser cookies \u2014 trying anonymous download")
            attempts = (None,)

        for browser in attempts:
            opts = base_opts(ffmpeg_path, output_dir)
            opts['tmp_dir'] = tempfile.mkdtemp(prefix="ytdlp_")
            opts['cleanup_tmp_files'] = True
            tmp_dirs.append(opts['tmp_dir'])
            if browser:
                opts['cookiesfrombrowser'] = (browser, None, None, None)

            try:
                with yt_dlp.YoutubeDL(opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                break
            except yt_dlp.utils.DownloadError as e:
                last_error = str(e)
                if is_network_error(last_error):
                    break
                if browser:
                    print(f"\u26a0\ufe0f  Cookies from {browser} didn't work, trying next option...")
                continue
        else:
            report_error(last_error or "extraction failed")
            return

        if info is None:
            print("\n\u274c Could not extract video info (private, deleted, or unsupported URL?)")
            return
        if 'entries' in info:
            info = info['entries'][0]
        req = info.get('requested_downloads') or []
        filename = req[0]['filepath'] if req else ydl.prepare_filename(info)
        print(f"\n\u2728 Download completed: {filename}")
    except Exception as e:
        print(f"\n\u274c Unexpected error: {e}")
    finally:
        for tmp in tmp_dirs:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter the URL: ").strip()
    download(url)
