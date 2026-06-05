---
title: "Welcome"
date: 2025-11-08
draft: false
---

### Student Grouping Algorithm Overview

  

This algorithm is designed to take student records (including class, gender, department, and GPA) organized by class, and partition them into isolated groups of 5, while maximizing the internal diversity of each group across multiple metrics.

  

#### Core Process

  

The algorithm proceeds in two main phases: a **Constructive Greedy Phase** and a **Local Improvement Phase**.

  

1.  **Data Organization and Preprocessing (OOP)**

    * **Structuring:** An Object-Oriented Programming (OOP) approach is used to encapsulate data and logic. Student information, group state, and grouping mechanics are handled by `Student`, `Group`, and `GroupingEngine` classes, ensuring high cohesion.

    * **Isolation:** The grouping process runs **independently for each class** in the CSV file, strictly ensuring that all members of a group belong to the same class.

    * **Pre-Sorting:** Before assignment begins, students within each class are sorted in **descending order by GPA**. This serves as the foundation for **GPA balancing**, forcing high and low achievers to be dispersed among the initial set of groups.

  

2.  **Initial Grouping (Greedy Assignment)**

    * **O(1) Diversity Scoring:** To overcome performance bottlenecks in the greedy phase, the `Group` object maintains real-time internal statistics (member count, gender counts, unique department set, etc.). This allows the calculation of the **Diversity Score** after adding a new student to be performed in **O(1)** time.

    * **Heuristic Selection:** Students from the sorted list are processed sequentially. For each student, the algorithm **iterates through all non-full groups** to calculate the **Composite Diversity Score** (weighted average of Department and Gender scores) if the student were to join.

    * **Greedy Decision:** The student is assigned to the group that yields the **highest Composite Diversity Score**. Ties are broken by prioritizing the group with the current lowest number of members to maintain uniform group size.

  

3.  **Pairwise Swapping Optimization (Local Improvement)**

    * **Mitigating Greedy Limitations:** Since the initial greedy phase only guarantees a local optimum, a **Pairwise Swapping** (local search) optimization is introduced to seek a globally better solution.

    * **Iterative Refinement:** Over a set number of iterations (e.g., 5000), the algorithm randomly selects two distinct groups ($G_A, G_B$) within the same class and two members ($S_A \in G_A, S_B \in G_B$).

    * **Acceptance Criteria:** The algorithm calculates the **total diversity score** of the two groups if $S_A$ and $S_B$ were swapped. If the new score is an improvement over the old one, the swap is executed. This process continually iterates, allowing the solution to settle near a high-quality approximate optimum.

  

#### Evaluation Metrics

  

The algorithm's effectiveness is assessed by quantifying diversity, where higher scores indicate better grouping:

  

* **Gender Score:** $1 - \frac{|\text{Male Count} - \text{Female Count}|}{\text{Group Size}}$ (Closer to 1.0 is best)

* **Department Score:** $\frac{\text{Unique Depts Count}}{\text{Group Size}}$ (Closer to 1.0 is best)

* **GPA Balance:** The **Variance** of GPAs within the group (Maximization desired)

  

Please note that:

1. based on my habit, class refers to the tut group in the title, department refers to the school in the title, and GPA refers to the CGPA in the title, group refers to team in the title. These differences have been fixed in the input and output interfaces of the code;

2.The current grouping pattern is roughly G1, G2...G10; G1, G2...G10;... However, since the classes are isolated and there seems to be no requirement for the group numbers to be sequential (1 2 3 4 5 ...10, 11, 12...), perhaps you can directly modify the output part of the code to require the class name and the output group name to be spliced ​​together, and the spliced ​​new name is used as the group name.

Writtern by Liu Haiheng