# Finding 14 - File Upload Bypass

## Exploitability
Moderate to Hard. Exploiting this requires knowledge of crafting HTTP requests and basic understanding of how to bypass file upload restrictions. However, it can be done using tools like curl or browser developer tools.

## Risk level/type

OWASP top 10 :
- A03:2021 - Injection
    => "User-supplied data is not validated, filtered, or sanitized by the application."


## Detailed description of the exploit
- **Understand the upload restriction:**
    - The upload page only accepted files with a .jpg extension. Other file types were rejected.
- **Bypass the extension restriction:**
    - Using the ```curl``` command, we crafted an HTTP POST request that submitted a malicious file (```webshell.php```) while claiming it was a valid image file (```image/jpeg```).
    - the command used: ```curl -s -X POST -F "uploaded=@webshell.php;type=image/jpeg" -F "Upload=Upload" "http://192.168.56.101//index.php?page=upload" | grep 'flag'  ```
    - ```@webshell.php```: This indicates the file being uploaded.
    - ```type=image/jpeg```: This tricks the server into believing the file is a JPEG image by setting the MIME type manually.
- **Upload**
    - The server only checked the MIME type and/or file extension but did not validate the file's actual content.

## Impact

- **Remote code execution:**
    - If attackers upload a malicious script (e.g., a PHP web shell), they can execute arbitrary commands on the server, potentially gaining full control over it.
- **Data exfiltration and manipulation:**
    - Attackers could read or modify sensitive files, access the database, or exfiltrate sensitive data.

## Remediation
1. **Server-side file validation:**
    - Validate the uploaded file's content and extension on the server side. Example: Check the actual file type by inspecting the file signature (also called magic bytes). For example, a valid JPEG file starts with FFD8FF in hexadecimal.
2. **Limit the upload directory:**
    - Store uploaded files in a directory outside the webroot to prevent them from being executed.
3. **Rename files on upload:**
    - Assign random names and strip extensions to prevent attackers from executing scripts.
    - For example, save the uploaded file as random_id instead of webshell.php.
4. **MIME type verification:**
    - Rely on server-side libraries (e.g., PHP’s finfo, Python’s magic, or Node.js’s mime) to verify file types.

## Additional resources

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

OWASP File Upload Security Guide:
https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

MIME type validation guide:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
