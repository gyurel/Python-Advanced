def negative_vs_positive(nrs, neg, pos):
    for x in nrs:
        if x < 0:
            neg += x
        else:
            pos += x

    return neg, pos


negatives = 0
positives = 0

numbers = [int(x) for x in input().split()]

negatives, positives = negative_vs_positive(numbers, negatives, positives)

print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
