def extract_documents(tab):
    documents = []
    document = {}
    for line in tab:
        if line:
            values = line.split(' ')
            for value in values:
                v = value.split(':')
                document[v[0]] = v[1]
        else:
            documents.append(document)
            document = {}
    documents.append(document)

    return documents


def check_fields(document, required_fields):
    for field in required_fields:
        try:
            document[field]
        except KeyError:
            return False
    return True
