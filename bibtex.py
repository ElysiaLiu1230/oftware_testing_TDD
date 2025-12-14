def extract_author(author):
    parts = author.split()

    if len(parts) == 1:
        return parts[0], ""

    if len(parts) == 2:
        first, surname = parts
        return surname, first
    
    if "," in author:
        surname, first = author.split(",", 1)
        return surname.strip(), first.strip()

    # len(parts) > 2
    surname = parts[-1]
    first = " ".join(parts[:-1])
    return surname, first
