# Contributing to Hacktoberfest 2025 - Python Edition

First off, thank you for considering contributing to this Python project! 🎉🐍

## Table of Contents

- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Code Review Process](#code-review-process)

## Getting Started

1. **Fork the repository** to your own GitHub account
2. **Clone the project** to your machine
3. **Create a branch** locally with a succinct but descriptive name
4. **Commit changes** to the branch
5. **Push changes** to your fork
6. **Open a Pull Request** in our repository

### Prerequisites

- A GitHub account
- Git installed on your local machine
- Python 3.7 or higher installed
- Basic knowledge of Python programming

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps which reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include screenshots if possible

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- Use a clear and descriptive title
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Describe the current behavior and explain which behavior you expected to see instead
- Explain why this enhancement would be useful

### 📝 Python Code Contributions

#### Types of Contributions We Welcome

1. **Algorithm Implementations**
   - Sorting algorithms (bubble sort, merge sort, quick sort, etc.)
   - Search algorithms (binary search, linear search, etc.)
   - Data structure implementations (linked lists, trees, heaps, etc.)
   - Graph algorithms (BFS, DFS, Dijkstra's, etc.)
   - Dynamic programming solutions

2. **Utility Functions**
   - String manipulation functions
   - List/array operations
   - Mathematical functions
   - File operations
   - API wrappers
   - Data validation utilities

3. **Mini Projects**
   - CLI tools
   - Web scrapers
   - Data parsers
   - Automation scripts
   - Simple games

4. **Documentation**
   - README improvements
   - Code comments and docstrings
   - Tutorial additions
   - Example usage demonstrations

## Style Guidelines

### Python Style Guidelines

All contributions must follow these Python best practices:

- **Follow PEP 8**: Use the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- **Type Hints**: Include type hints for function parameters and return values
- **Docstrings**: Add comprehensive docstrings for all functions and classes
- **Naming Conventions**:
  - Use `snake_case` for function and variable names
  - Use `PascalCase` for class names
  - Use `UPPER_CASE` for constants
- **Comments**: Add inline comments for complex logic
- **Error Handling**: Include proper exception handling with specific exception types
- **Line Length**: Keep lines under 88 characters (Black formatter standard) or 79 (PEP 8)
- **Imports**: Group imports (standard library, third-party, local) and sort alphabetically

### Code Quality Requirements

- Write clear, readable, and maintainable code
- Include error handling where appropriate
- Write meaningful variable and function names
- Test your code with different inputs
- No unused imports or variables

```python
def calculate_fibonacci(n: int) -> list:
    """
    Calculate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: List containing Fibonacci sequence
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    # Implementation here
```

#### JavaScript
- Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- Use camelCase for variable and function names
- Include JSDoc comments for functions

```javascript
/**
 * Calculate the sum of an array
 * @param {number[]} arr - Array of numbers
 * @returns {number} Sum of all elements
 * @throws {TypeError} If input is not an array
 */
function calculateSum(arr) {
    if (!Array.isArray(arr)) {
        throw new TypeError('Input must be an array');
    }
    // Implementation here
}
```

#### Java
- Follow [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- Use camelCase for method and variable names
- Use PascalCase for class names
- Include Javadoc comments

```java
/**
 * Represents a binary search tree node.
 */
public class TreeNode {
    /**
     * Inserts a value into the tree.
     * @param value The value to insert
     * @return true if insertion was successful
     */
    public boolean insert(int value) {
        // Implementation here
    }
}
```

## Commit Message Guidelines

We follow a simple commit message format:

```
<type>: <subject>

<body>
```

### Types
- **Add:** New feature or file
- **Fix:** Bug fix
- **Update:** Changes to existing functionality
- **Docs:** Documentation only changes
- **Style:** Formatting, missing semicolons, etc.
- **Refactor:** Code change that neither fixes a bug nor adds a feature
- **Test:** Adding tests
- **Chore:** Updating build tasks, package manager configs, etc.

### Examples

```
Add: Implement bubble sort algorithm in Python

Added a bubble sort implementation with detailed comments
and example usage. Includes time complexity analysis.
```

```
Fix: Resolve index out of bounds error in binary search

Fixed edge case where the search function would fail on
empty arrays.
```

```
Docs: Update README with contribution guidelines

Enhanced the README with step-by-step instructions for
first-time contributors.
```

## Pull Request Process

1. **Ensure your code follows the style guidelines** of the language you're using
2. **Update the README.md** if you're adding a new language folder
3. **Add examples** of how to use your code in comments or a separate example file
4. **Test your code** thoroughly before submitting
5. **Fill out the pull request template** completely
6. **Link any relevant issues** in your pull request description
7. **Be responsive** to feedback and be prepared to make changes

### Pull Request Template

When you create a pull request, please include:

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] New feature (code contribution)
- [ ] Bug fix
- [ ] Documentation update
- [ ] Code refactoring

## Language/Category
- Language: [e.g., Python, JavaScript, Java]
- Category: [e.g., Algorithm, Utility, Mini Project]

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have commented my code where necessary
- [ ] I have tested my code thoroughly
- [ ] My changes don't break existing functionality
- [ ] I have updated documentation if needed
```

## Code Review Process

1. Maintainers will review your pull request within 2-3 days
2. Feedback will be provided as comments on the pull request
3. Make requested changes and push to the same branch
4. Once approved, your PR will be merged!

### What We Look For

- ✅ Code quality and readability
- ✅ Proper Python docstrings and type hints
- ✅ Following PEP 8 conventions
- ✅ Comprehensive error handling
- ✅ No duplicate contributions
- ✅ Meaningful contribution (not spam)
- ✅ Tested code with example usage

## Questions?

Don't hesitate to ask! You can:
- Open an issue with your question
- Comment on an existing issue or pull request
- Reach out to the maintainers

## Recognition

All contributors will be recognized in the README! Your contributions help make this project better for everyone. 🌟

---

Thank you for contributing! 🎉

Happy Hacking! 🚀
