import os

renames = {
    r"d:\eskoolwork\icseSyllabusQuestions\lmao.py": r"d:\eskoolwork\icseSyllabusQuestions\syllabus_practice.py",
    r"d:\eskoolwork\icseSyllabusQuestions\love.py": r"d:\eskoolwork\icseSyllabusQuestions\turtle_heart.py",
    r"d:\eskoolwork\icseSyllabusQuestions\Gigachad.jpg": r"d:\eskoolwork\icseSyllabusQuestions\syllabus_asset.jpg",
    r"d:\eskoolwork\vennD.py": r"d:\eskoolwork\venn_diagrams.py"
}

for old, new in renames.items():
    try:
        if os.path.exists(old):
            os.rename(old, new)
            print(f"Renamed {old} to {new}")
        else:
            print(f"File {old} not found.")
    except Exception as e:
        print(f"Failed to rename {old}: {e}")
