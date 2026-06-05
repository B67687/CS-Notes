---
title: "🕸️ Number Systems"
date: 2025-11-08
draft: false
---


From what I know, in number systems, when we count the number of things we start from 1. This makes sense because 1 is the first actual "thing" that we define something as, while 0 is no thing, or nothing. But when we want to measure distance from some point, we start from 0, because it makes sense that we start from no distance away from the start, and then begin to get distance.

> There are 2 properties of numbers that we think of that are exactly what I just said. One is the **counting property**, where we usually think of it as the amount of things (start from 1), and one is the **offset property**, which we know of as difference (start from 0). This links the property of numbers to my current knowledge of numbers.

## 🔗 The Relationship Between Count and Offset

Thus, for the same point in the number space, the count is always 1 more than the distance away from the start (0). This is the inherent relationship between count and offset, when the start is the same number.

Thus, for an array of numbers, the position, or index, is based off the distance from the starting position. This is the offset from the start, thus starting from 0, and the count is still the number of elements, which is one more than the index.

## 💻 The Programming Problem

Then we have the problem of creating arrays of numbers, how do we call its creation?

The first preference would have been to fix the range of numbers, for which we have the START and END. Let's say we want the range to be from 1 to 8, then we will just select START=1, END=8. And then we will select the constant offset between every next number, known as the STEP, because we step into the next number with this amount of steps. To simplify the example, we will use STEP=1, so we get 1 to 8.

- Python by default uses step 1, because it is what most people were thinking of.

We get very nice calls, so now the other property is to know how many numbers there are. We do this by taking the difference between the start and end and dividing by the step to get the actual difference. Because the counting number is always 1 more than its difference, we add 1 to that difference to yield the counting number.

## 💡 **The Optimization**

This may be fine for anyone, but for computer scientists, it is seen as a place that is worth to be optimized, as these calculations with a step of 1 will be done frequently, so we can squeeze as much as possible where we can.

The main point of optimization is to remove the need to add 1, such that taking the difference would be enough. This would mean either shifting the start back by 1, or the end in front by 1.

Shifting the start back by 1 would be kind of weird, because we usually think of starting from the number itself instead of starting behind the number. Society can change and that is simply a thought pattern we are intuitively used to. One can imagine exclusive start as a preparation step for when one actually starts, and similarly exclusive stop as seeing the barrier ahead to stop, and then stopping before hitting it. What is actually more problematic is that now for index 0 we have to account for -1, which I don't know if 2s complement solves that, but it is now another complication we have added to at least how we think about things.

If we shift the end forward by 1 instead, we don't have to account for the special -1 case. We just have to reshape our thinking to have the stop sign be in front of where we actually stop, so that we stop where we want to. This adds 1 point of difference in thinking instead of the 2 presented with shifting back by 1.

Now that we have it shifted forward by 1, we can simply find the count of the numbers to be `stop - start`, instead of `stop - start + 1`.
