"""Program to check if a URL is present in a string."""

def check_for_url_in_a_string():
    """Check if a URL exists in a given string."""
    test_strings = [
        "Visit https://www.geeksforgeeks.org for more info",
        "No URL here!",
        "Check out http://example.com and ftp://files.example.com",
    ]

    for s in test_strings:
        urls = []
        for prefix in ['https://', 'http://', 'ftp://']:
            start = 0
            while True:
                idx = s.find(prefix, start)
                if idx == -1:
                    break
                end = s.find(' ', idx)
                if end == -1:
                    end = len(s)
                urls.append(s[idx:end])
                start = end
        if urls:
            print(f'URLs found in "{s}": {urls}')
        else:
            print(f'No URL found in "{s}"')

if __name__ == "__main__":
    check_for_url_in_a_string()
