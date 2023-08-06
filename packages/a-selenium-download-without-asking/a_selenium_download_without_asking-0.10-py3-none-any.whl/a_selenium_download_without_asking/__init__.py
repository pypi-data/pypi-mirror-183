import os


def enable_download_without_asking(driver, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_dir},
    }
    command_result = driver.execute("send_command", params)
    return command_result
