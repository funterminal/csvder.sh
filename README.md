# CSVDER - Advanced Command Line CSV Renderer

## Overview

CSVDER is a powerful, beautiful command line utility designed for beautiful and efficient CSV file rendering. Built with Python and leveraging the Rich library, it provides an enhanced terminal experience for viewing and interacting with CSV data.

## Key Features

- **Rich Terminal Rendering**: Utilizes the Rich library for beautiful, formatted output with colors, tables, and panels
- **Interactive Interface**: Allows user interaction after initial file rendering
- **Search Functionality**: Full-text search across all columns
- **Data Preview Options**: View head or tail sections of the data
- **Responsive Layout**: Adapts to terminal size with intelligent overflow handling
- **Performance Optimized**: Handles large files with row limiting and efficient processing

## Installation

### Direct Download Method

```bash
wget https://raw.githubusercontent.com/funterminal/csvder.sh/refs/heads/main/src/csvder.py
chmod +x csvder.py
sudo mv csvder.py /usr/local/bin/csvder
```

### Python Package Requirements

CSVDER requires Python 3.7+ and the following packages:
- rich

Install dependencies with:

```bash
pip install rich
```

## Usage

### Basic Command Structure

```bash
csvder render <filename.csv>
```

### Command Line Options

| Option    | Description                          | Required |
|-----------|--------------------------------------|----------|
| render    | Action to perform                   | Yes      |
| filename  | Path to CSV file to render          | Yes      |

### Interactive Commands

After initial rendering, CSVDER provides an interactive prompt with these options:

1. **search** - Perform full-text search across all columns
2. **head** - View top N rows of the dataset
3. **tail** - View bottom N rows of the dataset
4. **exit** - Quit the application

## Technical Details

### File Handling

- Supports UTF-8 encoded files
- Validates file existence and content
- Handles empty files gracefully
- Processes standard CSV format with header row

### Rendering Engine

- Uses Rich's Table and Layout components
- Implements intelligent column width management
- Defaults to showing first 50 rows (configurable)
- Color-coded interface elements for better UX

### Performance Considerations

- Loads entire file into memory for interactive features
- Implements row limiting to prevent terminal overflow
- Efficient search implementation using list comprehensions

## Examples

### Basic File Rendering

```bash
csvder render data/sample.csv
```

### Interactive Session Example

```
CSVDER - Lightweight CSV Renderer
+-----+----------+-----------+
| ID  | Name     | Value     |
+-----+----------+-----------+
| 1   | Test     | 100.00    |
| 2   | Example  | 200.50    |
+-----+----------+-----------+
Showing first 2 rows out of 100 | Columns: 3

What would you like to do next? [search/head/tail/exit]: search
Enter text to search: Example

Search Results for 'Example'
+-----+----------+-----------+
| ID  | Name     | Value     |
+-----+----------+-----------+
| 2   | Example  | 200.50    |
+-----+----------+-----------+
```

## Error Handling

CSVDER provides clear error messages for:
- Missing or invalid files
- Empty CSV files
- Improper command usage
- Search queries with no results

## Contributing

Contributions are welcome. Please follow standard GitHub pull request process.

## Support

For issues or feature requests, please open an issue on the GitHub repository.