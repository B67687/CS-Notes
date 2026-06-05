
This document explains the purpose, logic, inputs, outputs, and edge cases of each function in the provided Python codebase.

---

## `load_data(file_path)`

### Purpose
Loads student data from a CSV file and organizes them by tutorial group.

### Inputs
- `file_path`: path to the CSV file containing student records.

### Outputs
- A dictionary mapping tutorial group names to lists of `Student` objects.
- Returns `None` if the file is not found.

### Line-by-Line
```python
students_by_class = defaultdict(list)
```
Initializes a dictionary where each key maps to a list by default.

```python
with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
```
Opens the file and reads it as a dictionary per row.

```python
for row in reader:
    student = Student(row)
    students_by_class[student.cls].append(student)
```
Creates a `Student` object from each row and appends it to the appropriate tutorial group.

```python
except FileNotFoundError:
    print(...)
    return None
```
Handles missing file gracefully.

### Edge Cases
- File missing → returns `None`
- Malformed CSV → may raise other exceptions not caught here

---

## `run_full_grouping_process(students_by_class)`

### Purpose
Groups students within each tutorial group using greedy assignment and local optimization.

### Inputs
- `students_by_class`: dictionary of tutorial groups to student lists

### Outputs
- `all_grouped_students`: list of all students with assigned teams
- `all_diversity_reports`: list of diversity metrics per group

### Line-by-Line
```python
for class_name, students in students_by_class.items():
    engine = GroupingEngine(students, group_size=5)
```
Initializes a grouping engine for each tutorial group.

```python
engine.run_greedy_assignment()
engine.run_local_swap_optimization(max_iterations=5000)
```
Performs greedy assignment followed by local optimization.

```python
all_grouped_students.extend(...)
all_diversity_reports.extend(...)
```
Collects results across all tutorial groups.

---

## `write_results_to_csv(data, file_path)`

### Purpose
Writes grouped student data to a CSV file.

### Inputs
- `data`: list of `Student` objects
- `file_path`: output CSV path

### Outputs
- None (writes to file)

### Line-by-Line
```python
if not data:
    print(...)
    return
```
Handles empty input gracefully.

```python
writer = csv.DictWriter(file, fieldnames=...)
writer.writeheader()
writer.writerows([s.to_dict() for s in data])
```
Writes header and rows using each student's `to_dict()` method.

### Edge Cases
- File write error → caught and printed

---

## `display_evaluation(reports)`

### Purpose
Prints average diversity metrics across all groups.

### Inputs
- `reports`: list of diversity metric dictionaries

### Outputs
- None (prints to console)

### Line-by-Line
```python
gender_scores = [r['gender_score'] for r in reports]
dept_scores = [r['dept_score'] for r in reports]
gpa_variances = [r['gpa_variance'] for r in reports]
```
Extracts individual metrics.

```python
print(...)
```
Prints formatted averages.

---

## `visualize_results(all_grouped_students, sample_class_name)`

### Purpose
Generates GPA and gender distribution plots for a selected class.

### Inputs
- `all_grouped_students`: list of all grouped students
- `sample_class_name`: name of the class to visualize

### Outputs
- None (displays plots)

### Line-by-Line
```python
class_data = [s for s in all_grouped_students if s.cls == sample_class_name]
```
Filters students by class.

```python
gpa_by_group = defaultdict(list)
gender_counts = defaultdict(lambda: defaultdict(int))
```
Prepares data structures for plotting.

```python
sns.boxplot(...)  # GPA distribution
ax.bar(...)       # Gender distribution
```
Generates visualizations using seaborn and matplotlib.

### Edge Cases
- Class not found → prints error and exits

---

## `main()`

### Purpose
Orchestrates the full pipeline: loading, grouping, writing, evaluating, and visualizing.

### Inputs
- None (uses hardcoded file paths)

### Outputs
- None (side effects only)

### Line-by-Line
```python
students_by_class = load_data(INPUT_FILE)
if not students_by_class: return
```
Loads data and exits early if failed.

```python
all_grouped_students, all_diversity_reports = run_full_grouping_process(...)
write_results_to_csv(...)
display_evaluation(...)
visualize_results(...)
```
Runs the full grouping and reporting pipeline.
