def extract_author(author):
    parts = author.split()

    if len(parts) == 2:
        first, surname = parts
        return surname, first

    return author, ""
