def timeRequiredToBuy(tickets, k: int) -> int:
    time = 0
    for index, ticket in enumerate(tickets):
        time += min(tickets[k], ticket) if index <= k else min(tickets[k] - 1, ticket)
    return time
