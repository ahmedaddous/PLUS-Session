# PLUS Session Materials — MATH 1554: Linear Algebra

Worksheets, slides, solutions, and session plans I wrote as a **PLUS** (Peer-Led Undergraduate Study) leader for **MATH 1554: Linear Algebra** at Georgia Tech, covering the **Summer 2023** and **Fall 2023** semesters.

PLUS sessions are optional, peer-led study sessions that run alongside the lectures. Each session goes back over recent material through group work, practice problems, and short concept reviews. The materials here were made for those sessions. They supplement the official course and **are not official course materials**.

- **Fall 2023 course site:** [MA 1554 Linear Algebra (Fall 2023)](https://sbarone7.math.gatech.edu/ma1554f23.html), which has the lecture notes, schedule, and practice exams. (Instructor: Dr. Salvador Barone.)
- **Summer 2023:** there is no public course site for this semester.

Section numbers (for example *1.5* or *6.5*) refer to sections of the course textbook, as used in the MATH 1554 lecture schedule.

---

## Repository layout

```
.
├── su2023/          # Summer 2023, organized by textbook sections
│   ├── 1.3-1.9/
│   ├── 2.1-2.9/
│   ├── 3.1-3.3/
│   ├── 5.1-5.5/
│   ├── 6.1-6.5/
│   ├── 7.1-7.4/
│   └── Final Exam Review/
└── fa2023/          # Fall 2023, organized by week, then by session
    ├── Week 2/
    │   ├── Tuesday (1.1-1.4)/
    │   └── Thursday (1.5)/
    ├── ...
    └── Week 14/
```

Each session folder usually holds some of the following:

| File | What it is |
|---|---|
| `worksheet*.tex` / `.pdf` | The handout students work through during the session |
| `solutions.tex` | Worked solutions. It is pulled into the worksheet with `\include{solutions}`, so compiling the worksheet gives a PDF with solutions at the end |
| `session_plan.tex` / `.pdf` | My outline for running the session: the opening activity, how groups collaborate, and what each activity is meant to achieve |
| Topic slides (`diagonalization.tex`, `least_squares.tex`, …) | Beamer slides for a short concept review |
| `double_worksheet_*.tex` | Worksheets for longer "Double PLUS" exam-review sessions |

---

## Summer 2023

| Folder | Sections | Topics | Contents |
|---|---|---|---|
| `1.3-1.9` | 1.3–1.9 | Span and vector equations, the matrix equation, solution sets, linear independence, linear transformations | Worksheet |
| `2.1-2.9/2.1-2.5` | 2.1–2.5 | Matrix operations, inverses, the Invertible Matrix Theorem, partitioned matrices, LU factorization | Worksheet, a shorter "reduced" worksheet, solutions, formula sheet, LU slides (`.pptx`), outline (`.docx`) |
| `2.1-2.9/2.8-2.9` | 2.8–2.9 | Subspaces, basis, dimension, rank | Slides (`.pptx`) and a [Manim](https://www.manim.community/) animation of the span of a vector (`main.py`) |
| `3.1-3.3` | 3.1–3.3, 4.9 | Determinants, Markov chains | Worksheet, solutions, slides on determinants and Markov chains |
| `5.1-5.5/5.1-5.2` | 5.1–5.2 | Eigenvalues and eigenvectors, the characteristic equation | "Eigen-*stuff*" slides, Exam 2 review, solutions |
| `5.1-5.5/5.3-5.5` | 5.3–5.5 | Diagonalization, complex eigenvalues | Worksheet, solutions, slides, session plan, Exam 3 review |
| `6.1-6.5/6.1-6.4` | 6.1–6.4 | Inner products, orthogonality, orthogonal projections, Gram–Schmidt | Worksheet, solutions, slides, session plan |
| `6.1-6.5/6.5` | 6.5 | Least squares | Slides, Exam 3 review, solutions, session plan |
| `7.1-7.4` | 7.1–7.4 | Symmetric matrices, quadratic forms, constrained optimization, SVD | Slides on orthogonal diagonalization and quadratic forms, session plan |
| `Final Exam Review` | All | Cumulative review | Review worksheet, solutions, session plan |

---

## Fall 2023

| Week | Session | Sections | Topics |
|---|---|---|---|
| 2 | Tuesday | 1.1–1.4 | Systems of linear equations, row reduction, vector and matrix equations |
| 2 | Thursday | 1.5 | Solution sets of linear systems |
| 3 | Tuesday | 1.7 | Linear independence |
| 3 | Thursday | 1.8 | Linear transformations |
| 3 | **Sunday (Double)** | — | **Exam 1 review** |
| 4 | Tuesday | 2.2–2.3 | Matrix inverses, the Invertible Matrix Theorem |
| 4 | Thursday | 2.4–2.5 | Partitioned matrices, LU factorization |
| 5 | Tuesday | 2.8–2.9 | Subspaces, dimension, rank |
| 5 | Thursday | 3.1–3.3 | Determinants |
| 6 | Tuesday | 5.1, 5.9 | Eigenvectors, Markov chains |
| 6 | **Thursday (Double)** | — | **Exam 2 review** |
| 8 | Tuesday | 5.3 | Diagonalization |
| 8 | Thursday | 5.5 | Complex eigenvalues |
| 9 | Tuesday & Thursday | 6.1–6.2 | Inner products, orthogonal sets |
| 10 | Tuesday | 6.3–6.4 | Orthogonal projections, Gram–Schmidt |
| 10 | Thursday | 6.5 | Least squares |
| 11 | **Monday (Double)** | — | **Exam 3 review** |
| 12 | Tuesday | 7.1 | Symmetric matrices, orthogonal diagonalization |
| 12 | Thursday | 7.2 | Quadratic forms |
| 13–14 | Tuesday | 7.3–7.4 | Constrained optimization, singular value decomposition |

The Double PLUS exam reviews were written together with fellow PLUS leaders **Nora Butler** and **Sri Palaniappan**.

---

## Using the Materials

**Just reading?** Every session has compiled PDFs next to its `.tex` sources, so you can open those directly.

**Rebuilding from source:** the documents are standard LaTeX (`article` for worksheets and plans, `beamer` for slides) and rely on common packages such as `amsmath`, `amssymb`, `fancyhdr`, `booktabs`, `bm`, `enumitem`, and `pgfplots`. Any recent TeX Live or MiKTeX install, or Overleaf, should be enough:

```bash
cd "fa2023/Week 2/Tuesday (1.1-1.4)"
pdflatex worksheet11-14.tex   # pulls in solutions.tex
```

**Manim animation (Summer 2023, 2.8–2.9):**

```bash
cd "su2023/2.1-2.9/2.8-2.9"
manim -pql main.py RepresentSubspace
```

---

## Disclaimer

These are my own study materials. They are not affiliated with or endorsed by the MATH 1554 instructors or the Georgia Tech School of Mathematics. Errors are possible, so check anything important against your lecture notes and textbook. If you find a mistake, please open an issue.

## Author

**Ahmed Mohammed**, PLUS Leader for MATH 1554 in Summer and Fall 2023.
