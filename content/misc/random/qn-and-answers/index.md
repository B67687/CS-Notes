---
title: "Qn and Answers"
date: 2025-11-08
draft: false
---

**Qn: Challenges from Not Being Allowed to Use NumPy and Pandas:**
 
The primary challenges involved development overhead and time complexity due to using custom solutions instead of standard libraries.

 **Custom Code Complexity:** Relying on custom methods for team operations makes seemingly simple changes, like implementing a fixed number of members per group (K), very complex. It requires writing extensive custom logic to handle group boundaries and edge cases.

 **Computational Efficiency:** The current time complexity is estimated as O((n^2)/K + I) or O(n^2) when simplified. Standard libraries like NumPy and Pandas, optimized for matrix and array operations, could likely offer faster execution times for large student datasets by improving efficiency compared to hand-coded list operations. But it might also actually take more space complexity top achieve similar results handcoded

---

**Qn: If You Had More Time, What Other Improvements Would You Make?** 

Given more time, the two most impactful improvements would focus on achieving a better global solution and a more balanced scoring system.

**Global Optimization (K-Reshuffling):** Since the algorithm can get stuck in a local optimum (a good, but not best, solution), the fix is to run the entire grouping process K number of times independently. You would then select the absolute best result from these K attempts, significantly improving the stability and quality of the final solution. This increase space complexity by the number of students in a group.

**Refined Scoring Weights:** Dedicate time to parameter tuning to address the scoring conflict. The goal is to make the benefit of optimizing GPA (a continuous variable) comparable to the benefit of optimizing gender/department (discrete variables). This would involve carefully adjusting the weights (factor_\*) to ensure that the algorithm properly considers and acts upon changes in GPA balance, rather than prioritizing demographic factors alone.

---

**Qn What Can Be Improved? (Reflection)****

The main area for improvement is achieving a finer and more granular balance of student GPAs within groups.

**GPA Imbalance:** The algorithm is good at balancing the average GPA across teams but struggles to balance the composition of scores (i.e., making sure each group has a similar mix of high, medium, and low GPAs).

**Scoring Conflict:** The score's reward for optimizing GPA variance and range is currently too low compared to optimizing discrete factors like gender or department diversity. The algorithm tends to prioritize gender and department changes because their impact on the total score is more immediate and significant.