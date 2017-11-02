import sys

def safe_error_decorator(run_func):
    """
    decorator to be used by plugins to wrap their data fetching functions
    """
    def safe_run(*args, **kwargs):
        try:
            data = run_func(*args, **kwargs)
            return data
        except Exception as e:
            print("Failed: %s" % e)
            sys.exit(1)
    return safe_run
        
class FetchError(Exception):
    def __init__(self, request, reason):
        """
        Fetch Error wraps Requests Errors, specifically to be used for
        Non 200 status code Errors, Invalid JSON parse Error
        """
        self.r = request
        self.reason = reason
    def __str__(self):
        return "Fetch failed [status= %d]\nReason: %s" % (self.r.status_code, self.reason)
