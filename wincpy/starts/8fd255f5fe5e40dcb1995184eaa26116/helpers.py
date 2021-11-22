from hashlib import sha3_512


def get_users():
    """Note that this way of storing usernames and passwords is nothing like
    how it would be done in a real application, but it suffices for this
    exercise application."""

    return {
        "Alice": "b778a39a3663719dfc5e48c9d78431b1e45c2af9df538782bf199c189dabeac7680ada57dcec8eee91c4e3bf3bfa9af6ffde90cd1d249d1c6121d7b759a001b1",
        "Bob": "d07e870dbf957e794c53fe56b0940d75c6b752096f59a90aaa31b4a420593fc5c520a2f51e884c34756e2445cfe2edce86ae566d22031bd02390a18c0fe0a63b",
    }


def hash_password(password):
    return sha3_512(password.encode("utf-8")).hexdigest()
