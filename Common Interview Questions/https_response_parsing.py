'''
HTTP Response Parsing

You are given a raw HTTP response as a string. Parse the response into a structured
representation containing the HTTP status code, headers, and body.

An HTTP response has the following format:

HTTP/1.1 <status_code> <status_message>
Header-Name: Header-Value
Header-Name: Header-Value
...
<blank line>
<body>

For example:

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 13

{"id": 12345}

The response consists of:

1. A status line containing:
   - HTTP version
   - numeric status code
   - status message

2. Zero or more headers.
   Each header is formatted as:

   Header-Name: Header-Value

3. A blank line separating the headers from the body.

4. An optional body.

Task

Implement the following function:

parse_response(response)

The function should return a dictionary with the following structure:

{
    "status_code": 200,
    "status_message": "OK",
    "headers": {
        "Content-Type": "application/json",
        "Content-Length": "13"
    },
    "body": '{"id": 12345}'
}

Requirements

- The first line is always the status line.
- Headers appear after the status line.
- The first blank line separates the headers from the body.
- Header names and values are separated by the first ":" character.
- Header values may contain additional ":" characters.
- There may be zero or more headers.
- The body may be empty.
- Preserve the header values as strings.
- Assume the input is otherwise well-formed.

Example 1

Input:

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 13

{"id": 12345}

Output:

{
    "status_code": 200,
    "status_message": "OK",
    "headers": {
        "Content-Type": "application/json",
        "Content-Length": "13"
    },
    "body": '{"id": 12345}'
}

Example 2

Input:

HTTP/1.1 404 Not Found
Content-Type: text/plain

Not Found

Output:

{
    "status_code": 404,
    "status_message": "Not Found",
    "headers": {
        "Content-Type": "text/plain"
    },
    "body": "Not Found"
}

Example 3

Input:

HTTP/1.1 204 No Content


Output:

{
    "status_code": 204,
    "status_message": "No Content",
    "headers": {},
    "body": ""
}


Constraints

- 1 <= length(response) <= 10^5
- The response contains valid HTTP formatting.
- Header names contain no ":" characters.
- The status code is a three-digit integer.

Your solution should run in O(n) time, where n is the length of the response.
'''

def read_response(res):
    output = {}
    lines = res.split("\n")

    status = lines[0]
    status = status.split(" ")
    output["status_code"] = status[1]
    output["status_message"] = " ".join(status[2:])
    output["headers"] = {}
    output["body"] = ""

    for l in range(1, len(lines)):
        curr = lines[l].split(" ")
        print(curr[0])
        if curr[0] == "Content-Type:":
            output["headers"]["Content-Type"] = curr[1]
        elif curr[0] == "Content-Length:":
            output["headers"]["Content-Length"] = curr[1]
        else:
            output["body"] = lines[l]
            

    return output

print(read_response("HTTP/1.1 200 OK\nContent-Type: application/json\nContent-Length: 13"))
print(read_response("HTTP/1.1 404 Not Found\nContent-Type: text/plain\nNot Found"))
print(read_response("HTTP/1.1 204 No Content"))
