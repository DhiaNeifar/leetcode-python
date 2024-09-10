def main(details):
    return len([x for x in details if int(x[11: 13]) > 60])
