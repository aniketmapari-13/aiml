# Forward and Backward Chaining
facts = {"fever", "cough", "fatigue"}
rules = [
    (["fever", "cough"], "flu_like"),
    (["flu_like", "fatigue"], "rest_recommended")]
# Forward Chaining: Facts -> Rules -> Goal
def forward_chaining(goal):
    known = facts.copy()
    seq = []
    changed = True
    while changed:
        changed = False
        for condition, result in rules:
            if all(c in known for c in condition) and result not in known:
                known.add(result)
                seq.append(f"{condition} -> {result}")
                changed = True
    return goal in known, seq
# Backward Chaining: Goal -> Rules -> Facts
def backward_chaining(goal):
    seq = []
    def prove(g):
        if g in facts:
            return True
        for condition, result in rules:
            if result == g:
                if all(prove(c) for c in condition):
                    seq.append(f"{condition} -> {result}")
                    return True
        return False
    result = prove(goal)
    seq.reverse()
    return result, seq
# Test
goal = "rest_recommended"
result, seq = forward_chaining(goal)
print("Forward Chaining:")
for s in seq:
    print(s)
print("Goal proved:", result)
result, seq = backward_chaining(goal)
print("\nBackward Chaining:")
for s in seq:
    print(s)
print("Goal proved:", result)
