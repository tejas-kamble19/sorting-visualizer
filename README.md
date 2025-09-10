# Sorting Algorithm Visualizer

An interactive Python application that visualizes popular sorting algorithms with step-by-step animations, time/space complexity analysis, and performance comparisons. Perfect for learning algorithmic concepts and demonstrating programming skills to recruiters!

## 🚀 Why This Project?

Recruiters love this because it shows:
- **Algorithmic thinking** - Understanding of fundamental sorting algorithms
- **UI/UX skills** - Clean, interactive graphical interface
- **Complexity analysis** - Real-time performance metrics and comparisons
- **Software engineering** - Well-structured, maintainable code architecture

## ✨ Features

### Core Functionality
- **6 Sorting Algorithms**: Bubble, Insertion, Selection, Merge, Quick, Heap Sort
- **Step-by-step Visualization**: Animated bar graphs showing algorithm progress
- **Complexity Analysis**: Real-time time/space complexity display
- **Performance Comparison**: Side-by-side algorithm performance on same dataset
- **Interactive Controls**: Speed adjustment, array size control, pause/resume
- **Custom Data Input**: Upload your own datasets (student scores, product prices, etc.)

### Visual Features
- **Color-coded Animation**: Different colors for comparing, swapping, sorted elements
- **Smooth Animations**: Matplotlib-based smooth transitions
- **Responsive Interface**: Clean Tkinter GUI with modern aesthetics
- **Real-time Metrics**: Operation counters and timing information

## 🛠 Tech Stack

- **Python 3.8+** - Core programming language
- **Tkinter** - GUI framework for the main interface
- **Matplotlib** - Chart visualization and animations
- **NumPy** - Array operations and data generation
- **Threading** - Non-blocking animations and user interactions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Extract the project files**
   ```bash
   unzip sorting_visualizer.zip
   cd sorting_visualizer
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

### One-Command Setup
```bash
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python main.py
```

## 📖 How to Use

1. **Launch** the application by running `python main.py`
2. **Select** a sorting algorithm from the dropdown menu
3. **Adjust** array size (10-200 elements) and animation speed
4. **Generate** random data or input your own dataset
5. **Start** the visualization and watch the algorithm work step-by-step
6. **Analyze** the complexity metrics displayed in real-time
7. **Compare** different algorithms on the same dataset

### Keyboard Shortcuts
- `Space` - Start/Pause animation
- `R` - Reset to original array
- `G` - Generate new random array
- `Esc` - Stop current animation

## 🧮 Algorithm Complexity Analysis

| Algorithm      | Best Case   | Average Case | Worst Case  | Space | Stable | In-Place |
|---------------|-------------|--------------|-------------|-------|--------|----------|
| Bubble Sort   | O(n)        | O(n²)        | O(n²)       | O(1)  | ✅     | ✅       |
| Insertion Sort| O(n)        | O(n²)        | O(n²)       | O(1)  | ✅     | ✅       |
| Selection Sort| O(n²)       | O(n²)        | O(n²)       | O(1)  | ❌     | ✅       |
| Merge Sort    | O(n log n)  | O(n log n)   | O(n log n)  | O(n)  | ✅     | ❌       |
| Quick Sort    | O(n log n)  | O(n log n)   | O(n²)       | O(log n)| ❌   | ✅       |
| Heap Sort     | O(n log n)  | O(n log n)   | O(n log n)  | O(1)  | ❌     | ✅       |

## 🐛 Troubleshooting

### Common Issues

1. **ImportError: No module named 'tkinter'**
   - Solution: Install tkinter - `sudo apt-get install python3-tk` (Ubuntu/Debian)

2. **Matplotlib backend errors**
   - Solution: Install backend - `pip install tk` or set backend manually

3. **Animation too slow/fast**
   - Solution: Adjust speed slider or modify animation settings

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

---

⭐ **Perfect for showcasing to recruiters** - demonstrates algorithmic knowledge, UI skills, and software engineering practices!
