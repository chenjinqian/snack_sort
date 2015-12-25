README

what is this?
This is an algorithm in python to sort a list of number. I want to find a method which need less compair between numbers as possible(Nlog2(N)), and it should be steady in any conditions.
A computer do not know the number after it operate on it (unless the number information is reprented by the bit position of the storage, in this way no compair is needed. That's another excellent algorithm, but not suit for every conditions). The basic idea is this, is I have all numbers sorted but last one, then I only have to compair Nlog2(N) times to decide its position. It's pretty the most we can do. The position of the sorted sequence have information in it, only with that information we can do it quicker. If you have random list, and want to find out how big a number is in that list, there is nothing we can do except compir one by one.
If I have first half sorted, then I can use the information in it to accerate the rest half.  Any number within the range of sorted list, can be decide very quickly, and became one of that list. Any one out of the range can be detect within two step, and form another small random sequence, to be handel later using same method.
It's like a snack eating some strawberry/egg, it digest it quickly and make it part of itself. If things are out of its ability, it make that thing an egg and left it behand, in next arround, new snack show up and handle the left. Two small snack with same longth conect to make a bigger one, untile all list is sorted.

TODO
The movement of the number can be Nlog2(N), I have some idea, yet need to be done.
