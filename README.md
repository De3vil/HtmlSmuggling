# HtmlSmuggling
* HTML smuggling is a malicious technique used by hackers to hide malware payloads in an encoded script in a specially crafted HTML attachment or   web page. 
* The malicious script decodes and deploys the payload on the targeted device when the victim opens/clicks the HTML attachment/link.
* The HTML smuggling technique leverages legitimate HTML5 and JavaScript features to hide malicious payloads and evade security detections.

* The HTML smuggling method is highly evasive. It could bypass standard perimeter security controls like web proxies and email gateways, which only check for suspicious attachments like `EXE, DLL, ZIP, RAR, DOCX or PDF`
* Embeds the selected binary file `(exe, dll, docx, pdf, etc) `into the Javascript file. Obfuscates Javascript functions. This makes it difficult to decode javascript functions.

* Once a victim receives the email and opens the attachment, their browser decodes and runs the script, which then assembles a malicious payload directly on the victim’s device.
![](src/HTMLsmuggling-1.jpg)
