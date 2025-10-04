# 🎃 Hacktoberfest 2025 - Code Contribution Repository

![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2025-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![GitHub contributors](https://img.shields.io/github/contributors/WalkingDevFlag/Hacktoberfest-2025)

## 📖 About This Repository

Welcome to the Hacktoberfest 2025 Python Code Contribution Repository! This is a beginner-friendly project designed to help developers make their first open-source contributions during Hacktoberfest, focusing specifically on Python programming.

### 🎯 Project Goals
- Provide a welcoming space for first-time Python contributors
- Collect diverse Python code samples, algorithms, and utilities
- Help participants learn Git and GitHub workflows
- Foster a supportive open-source community
- Promote Python best practices and clean code

## 📂 Project Structure

```
Hacktoberfest-2025/
├── README.md              # You are here!
├── CODE_OF_CONDUCT.md     # Community guidelines
├── CONTRIBUTING.md        # Detailed contribution guide
├── LICENSE                # MIT License
├── .github/               # GitHub templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
└── python/                # Python code samples
    ├── README.md          # Python-specific guidelines
    └── hello_world.py     # Example contribution
```

## 🤝 How to Contribute

We welcome the following types of Python contributions:
- ✅ Algorithms (sorting, searching, graph algorithms, etc.)
- ✅ Data structures implementations
- ✅ Utility functions and helper scripts
- ✅ Bug fixes and improvements
- ✅ Documentation enhancements
- ✅ Code optimizations and refactoring

### 🚀 Step-by-Step Contribution Guide

#### 1. Fork the Repository
Click the "Fork" button at the top right of this page.

#### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR-USERNAME/Hacktoberfest-2025.git
cd Hacktoberfest-2025
```

#### 3. Create a New Branch
```bash
git checkout -b feature/your-contribution-name
```

#### 4. Make Your Changes
- Add your Python code in the `python/` folder
- Follow PEP 8 style guidelines
- Include type hints and docstrings
- Add comments for complex logic
- Test your code before committing

#### 5. Commit Your Changes
```bash
git add .
git commit -m "Add: Brief description of your contribution"
```

**Commit Message Format:**
- `Add: [description]` - for new features
- `Fix: [description]` - for bug fixes
- `Update: [description]` - for updates to existing code
- `Docs: [description]` - for documentation changes

#### 6. Push to Your Fork
```bash
git push origin feature/your-contribution-name
```

#### 7. Create a Pull Request
- Go to your fork on GitHub
- Click "New Pull Request"
- Fill in the PR template with details about your contribution
- Wait for review!

## 📝 Contribution Guidelines

### ✅ Good Contributions
- Well-documented code with comments
- Unique algorithms or utilities
- Code that follows language best practices
- Meaningful variable and function names
- Includes examples of usage
- Has proper error handling

### ❌ Invalid Contributions
- Duplicate code
- Spam or meaningless changes
- Plagiarized code
- Code without documentation
- Breaking existing functionality
- Incomplete implementations

### 📋 Code Quality Standards
- Follow PEP 8 Python style guide
- Add comprehensive docstrings explaining your code
- Include type hints for function parameters and return values
- Use meaningful variable and function names
- Use meaningful commit messages
- One feature per pull request
- Include example usage in your code

## 🎓 Example Contributions

### Algorithm Example
```python
def fibonacci(n: int) -> list[int]:
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list[int]: Fibonacci sequence
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence


if __name__ == "__main__":
    print(fibonacci(10))
```

### Data Structure Example
```python
class Stack:
    """
    A simple stack implementation using a list.
    
    Supports push, pop, peek, and is_empty operations.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._items: list = []
    
    def push(self, item) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
```

### Utility Function Example
```python
def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (ignoring case and non-alphanumeric characters).
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]
```

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please:
- ✨ Be respectful and considerate
- 🤝 Accept constructive criticism gracefully
- 🎯 Focus on what's best for the community
- ❤️ Show empathy towards other contributors
- 🚫 No harassment, discrimination, or inappropriate behavior

See our full [Code of Conduct](CODE_OF_CONDUCT.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Contributors

Thanks to all our amazing contributors! 🎉

<a href="https://github.com/WalkingDevFlag/Hacktoberfest-2025/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=WalkingDevFlag/Hacktoberfest-2025" />
</a>

## 📊 Repository Stats

![GitHub stars](https://img.shields.io/github/stars/WalkingDevFlag/Hacktoberfest-2025?style=social)
![GitHub forks](https://img.shields.io/github/forks/WalkingDevFlag/Hacktoberfest-2025?style=social)
![GitHub issues](https://img.shields.io/github/issues/WalkingDevFlag/Hacktoberfest-2025)
![GitHub pull requests](https://img.shields.io/github/issues-pr/WalkingDevFlag/Hacktoberfest-2025)

## 📞 Contact & Support

- 🐛 Create an [Issue](https://github.com/WalkingDevFlag/Hacktoberfest-2025/issues) for bug reports or feature requests
- 💬 Join our discussions in the [Discussions](https://github.com/WalkingDevFlag/Hacktoberfest-2025/discussions) tab
- ⭐ Star this repository if you find it helpful!

## 🎉 Hacktoberfest & Python Resources

### Hacktoberfest
- [Hacktoberfest Official Website](https://hacktoberfest.com/)
- [How to Create a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

### Python Resources
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Documentation](https://docs.python.org/3/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Real Python Tutorials](https://realpython.com/)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you contribute to Hacktoberfest!

---

**Happy Hacking! 🚀**

Made with ❤️ for Hacktoberfest 2025
