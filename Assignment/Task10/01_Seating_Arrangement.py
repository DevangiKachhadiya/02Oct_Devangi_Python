# Seating Arrangement Problem
'''You have N guests attending a dinner party. Each guest has exactly two preferred neighbors they'd
like to sit next to. Write a Python function that:
• Accepts the number of guests and their neighbor preferences.
• Determines a valid circular seating arrangement satisfying all preferences.
• If no arrangement is possible, clearly state that.
Input Example:
guests = {
 'Alice': ['Bob', 'Carol'],
 'Bob': ['Alice', 'David'],
 'Carol': ['Alice', 'David'],
 'David': ['Bob', 'Carol']
}
'''

# Problem: Given N guests and their neighbor preferences, determine a valid circular seating arrangement.
# Approach: Create a graph and check if a valid seating arrangement is possible using depth-first search (DFS).

def seating_arrangement(guests):
    def dfs(guest, arrangement, visited):
        if len(arrangement) == len(guests):
            if arrangement[0] in guests[arrangement[-1]]:
                return arrangement
            return None
        for neighbor in guests[guest]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, arrangement + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    for guest in guests:
        arrangement = dfs(guest, [guest], {guest})
        if arrangement:
            return arrangement
    return "No valid arrangement possible"

guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}
print(seating_arrangement(guests)) 
