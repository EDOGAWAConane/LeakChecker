import requests
import hashlib
import sys

def request_api_data(query_char):
    """
    Request data from the Pwned Passwords API for a specific hash prefix.

    Args:
        query_char (str): The first 5 characters of the SHA1 hashed password.

    Returns:
        Response: The API response containing password hash suffixes and their occurrence counts.

    Raises:
        RuntimeError: If the API request fails (status code != 200).
    """
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}. Check the API and try again.')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    """
    Check if the provided password hash suffix exists in the list of hashes returned by the API.

    Args:
        hashes (Response): The API response containing hashed passwords and their counts.
        hash_to_check (str): The hash suffix of the password to check.

    Returns:
        int: The count of times the password was found in breaches. Returns 0 if not found.
    """
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return int(count)
    return 0

def pwned_api_check(password):
    """
    Check if a password has been exposed in data breaches using the Pwned Passwords API.

    Args:
        password (str): The plain-text password to check.

    Returns:
        int: The number of times the password has been found in breaches.
    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    """
    Main function to check multiple passwords against the Pwned Passwords API.

    Args:
        args (list): List of plain-text passwords provided via command-line arguments.

    Prints:
        Results for each password indicating if it was found in breaches and how many times.
    """
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... It\'s time to change it!')
        else:
            print(f'{password} was not found. You can keep it for now.')

if __name__ == '__main__':
    # Exit with the result of the main function. Pass command-line arguments (excluding script name).
    sys.exit(main(sys.argv[1:]))