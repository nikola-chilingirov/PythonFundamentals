n = int(input())
positives = []
counter_positives = 0
negatives = []
counter_negatives_sum = 0
for i in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
        counter_positives += 1
    else:
        negatives.append(num)
        counter_negatives_sum += num
print(positives)
print(negatives)
print(f"Count of positives: {counter_positives}")
print(f"Sum of negatives: {counter_negatives_sum}")