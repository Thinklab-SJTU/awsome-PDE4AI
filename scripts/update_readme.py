import json

def generate_readme():
    with open('data/papers.json', 'r', encoding='utf-8') as f:
        papers = json.load(f)

    lines = [
        '# Awesome AI4PDE',
        '',
        '![Banner](assets/banner.png)',
        '',
        '> 📚 A curated list of papers and resources on applying Artificial Intelligence to Partial Differential Equations (AI4PDE).',
        '',
        '## 📄 Papers',
        '',
        '| Title | Authors | Year | Link |',
        '|-------|---------|------|------|'
    ]

    for paper in papers:
        title = paper['title']
        authors = ', '.join(paper['authors'])
        year = paper['year']
        link = f"[Paper]({paper['link']})"
        lines.append(f"| {title} | {authors} | {year} | {link} |")

    lines.extend([
        '',
        '## 🔧 How to Contribute',
        '',
        'Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to add new papers.',
        '',
        '## 📜 License',
        '',
        'This project is licensed under the MIT License.'
    ])

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == '__main__':
    generate_readme()
