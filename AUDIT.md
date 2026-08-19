# Project and Course Audit: Practical Numerical Methods with Python

**Audit date:** 17 August 2026; second-pass update 18 August 2026  
**Repository state audited:** `b8a17ce` on `origin/master` (working branch: `codex/audit`)  
**Recommendation:** preserve this repository as the legacy edition and build a tested, accessible, agent-ready 2026 course in a fresh repository under the same organization.

## Executive summary

This repository contains an unusually coherent, problem-driven introduction to numerical methods. The phugoid, traffic-flow, diffusion, and elliptic-problem narratives remain valuable. The progression from physical model to discretization, implementation, convergence, stability, and interpretation is the asset to preserve.

It is not currently a reliable, self-contained course distribution. The only environment specification targets Python 3.4 and 2015 packages; all notebooks advertise custom Python 3.6 kernels; there is no CI, test suite, publication build, current assessment path, or agent-use policy; and 10 of 26 notebooks stop during a clean execution against the available Python 3.11 scientific stack. The retired Open edX instance removed the quizzes, grading, discussions, and badge path referenced by the module documentation. A learner can read much of the material, but cannot follow one authoritative setup-and-completion route with a defined outcome.

The right modernization is not merely to update syntax. In 2026, an engineer increasingly specifies work to coding agents, grants tools and data access, reviews generated changes, and proves that results are numerically and physically credible. The course should therefore keep teaching numerical reasoning while changing the computational workflow from “type this implementation” to “specify, delegate, inspect, test, validate, and communicate.” Agents should be allowed in substantial parts of the course, but the assessments must measure model formulation, verification, engineering judgment, provenance, and the ability to detect plausible but wrong results.

This audit now assumes a **new-edition repository**, not an in-place rewrite. Findings below describe what should inform selection and migration into that repository. The legacy README, installation instructions, notebooks, and visual assets should remain historical records; no broad remediation campaign is recommended here. Apart from this audit and small repository-hygiene fixes, further changes to the legacy repository should be limited to exceptional archival or security needs.

### Overall assessment

| Area | Assessment | Summary |
|---|---:|---|
| Mathematical and physical content | Strong | The five-module applied narrative remains distinctive and reusable. |
| Pedagogy | Good foundation, incomplete delivery | Explanations and experiments are strong; learning outcomes, rubrics, feedback, and current assessments are missing. |
| Reproducibility | Critical | Unsupported environment, custom kernels, runtime network and codec assumptions, no lock file or container. |
| Software quality | Weak | Most reusable logic lives in notebooks; there are no tests, CI checks, packaging metadata, or release process. |
| Accessibility | Critical | Missing image alternatives, animation-only explanations, old custom styling, and no documented caption/transcript review. |
| Licensing and provenance | Needs resolution | Top-level instructional license says CC BY 3.0 while notebook banners say CC BY 4.0. |
| 2026 agent readiness | Absent | No `AGENTS.md`, task specifications, executable acceptance tests, AI-use policy, provenance format, or guarded tool-access exercises. |
| Modernization potential | Excellent | The models have exact solutions, invariants, convergence expectations, and benchmark cases that are ideal for teaching verification of agent-produced work. |

## Scope and method

The audit accounted for every tracked file in the current checkout and reviewed repository history and remote branches for stranded course material. It included:

- inventory and type/size checks for all 134 tracked files;
- structural inspection of all 26 notebooks (1,236 cells: 850 Markdown and 386 code);
- inspection of all onboarding and module documentation, four Python helper modules, the environment file, CSS, data archives, figures, license, and top-level README;
- clean execution of temporary copies of all 26 notebooks with their kernel overridden to the available `python3` kernel;
- a second execution of the 10 failing notebooks with errors allowed, to expose failures hidden after deliberate teaching errors;
- validation of all 77 statically discoverable local references (all resolved);
- validation of both NPZ archives;
- an automated request check of 158 unique HTTP(S) targets, followed by manual interpretation of high-impact results;
- static searches for obsolete APIs, stale platform instructions, tests, CI, packaging, accessibility signals, and maintenance files;
- review of recent history and unmerged remote branches.

The execution environment was Python 3.11 with NumPy 1.26.4, SciPy 1.13.1, SymPy 1.13.2, Matplotlib 3.9.2, Numba 0.60.0, IPython 8.27.0, and Notebook 7.2.2. This is a useful compatibility probe, not the recommended 2026 environment and not a NumPy 2.x certification. Mathematical formulas and claims were checked through execution, consistency, and representative inspection; this was not a new formal proof of every derivation.

## Repository inventory

| Material | Count | Audit note |
|---|---:|---|
| Tracked files | 134 | Approximately 13.7 MiB outside `.git`; Git history is approximately 69.6 MiB packed. |
| Jupyter notebooks | 26 | 22 lessons/support notebooks and 4 distinct assignment-oriented notebooks. A fifth assignment (Traffic) is described but has no distinct assignment notebook. |
| Notebook cells | 1,236 | 850 Markdown; 386 non-empty code cells. |
| Python modules | 4 | `phugoid.py`, `traffic.py`, `helper.py`, `multigrid_helper.py`. |
| Markdown files | 10 | Root README, four onboarding guides, five module READMEs. |
| Images/animations | 86 | 46 PNG, 23 SVG, 17 GIF; one exact duplicate image across modules. |
| Data archives | 2 | Both load successfully and contain finite `float64` arrays. |
| Supplementary file | 1 | A collaborator-authored PDF from a separate course is present but only loosely connected to this repository; it is outside the scope of the new-edition migration. |
| Environment files | 1 | `nm_python_env.yaml`, pinned to Python 3.4-era conda builds. |
| Styling files | 1 | Classic Notebook CSS/HTML/MathJax injection. |
| Tests, CI, package metadata | 0 | No tests, `.github/workflows`, `pyproject.toml`, current lock file, or build definition. |

### Course map

| Area | Current contents | Durable value |
|---|---|---|
| Getting started | Command line for OS X/Red Hat, obsolete Python/Jupyter installation, notebook basics, Git basics | Mostly retire rather than migrate. Carry forward only a short, current quick start and the concepts needed to run and review the new course. |
| Module 1 | Phugoid theory, Euler integration, convergence, second-order methods, rocket assignment | Excellent model-first ODE and verification sequence. |
| Module 2 | 1D convection, CFL, diffusion, Burgers equation | Strong foundation in finite differences, stability, vectorization, and symbolic work. |
| Module 3 | Conservation laws, traffic flow, classical schemes, MUSCL, Sod assignment | Strong finite-volume/conservation narrative and rich benchmark potential. |
| Module 4 | Python function behavior, explicit/implicit diffusion, 2D problems, Crank-Nicolson, Gray-Scott assignment | Strong boundary-condition and implicit-method sequence; assignment is visually compelling. |
| Module 5 | Laplace, Poisson, iterative methods, Numba, conjugate gradient, Stokes assignment | Strong bridge from discretization to solver choice and performance. |

### Maintenance signals

The repository has a substantial history (more than 1,100 commits), but no release tags. Most substantive lesson changes date to 2018 or 2019. The only commits after 2019 are a 2025 README edit and 2026 removal/archiving of stale Open edX and staff links. The 2026 timestamps on 14 notebooks therefore indicate link cleanup, not a current dependency, pedagogy, or reproducibility review. The new edition should begin with an explicit version and changelog rather than inheriting misleading signals of current compatibility.

## Ranked findings and recommended actions

Priorities are ordered by learner harm and modernization dependency. **P0** blocks a credible relaunch; **P1** is required for a high-quality 2026 course; **P2** improves durability and reach; **P3** is cleanup. Unless an action explicitly says otherwise, implement it in the new-edition repository after selecting the relevant legacy material for migration; do not retrofit it here.

| Rank | Priority | Finding | Evidence | Recommended action | Effort |
|---:|:---:|---|---|---|:---:|
| 1 | P0 | No supported, reproducible runtime | `nm_python_env.yaml` pins Python 3.4.3, IPython 3.2, NumPy 1.9.2, SciPy 0.15.1, Matplotlib 1.4.3, SymPy 0.7.6, and Numba 0.20.0. Notebook metadata targets Python 3.6.5-3.6.9 and two site-specific kernel names. | Target Python 3.13 as the compatibility floor, test 3.13 and 3.14, target NumPy 2.x, and commit one canonical lock-capable environment plus a container/browser fallback. Include `ffmpeg` or remove the codec dependency. | M |
| 2 | P0 | The notebook collection is not cleanly executable | 16/26 notebooks ran to completion in the compatibility probe; 10 stopped. Failures include Matplotlib API changes, absent `ffmpeg`, changed SymPy behavior, an intentional `NameError`, and a runtime data download. | Use these failures as migration tests. Port only selected notebooks, rewrite expected-error cells, execute every required new-edition notebook offline in CI, and fail on unexpected errors. | M |
| 3 | P0 | The course delivery and assessment path disappeared with Open edX | Module READMEs promise quizzes, grading, badges, evidence, and platform interactions that no longer exist. Assignment notebooks contain prompts but no public rubrics, autograding tests, or current submission route. | Publish a canonical course site and syllabus. Recreate low-stakes checks, assignment rubrics, reference outputs, instructor tests, completion criteria, and an explicit archival note for the old badge language. | L |
| 4 | P0 | Current assignments do not measure work that remains meaningful when agents can generate code | The surviving assessments primarily ask students to implement and report values. No task asks for agent supervision, provenance, adversarial review, uncertainty, or defense of correctness. | Redesign assessments around model specification, acceptance tests, invariants, grid/time convergence, error budgets, review of agent diffs, and short oral or written defense. Allow agents where the learning outcome is supervision; restrict them only where individual recall is the outcome. | L |
| 5 | P1 | There is no maintainable software layer | No `pyproject.toml`, `src/`, tests, linting, typing, CI, release process, or dependency automation. Algorithms are duplicated or embedded in stateful notebooks. | Move reusable solvers and models into a small tested package; keep notebooks as narrative clients. Add `pytest`, notebook execution, formatting/linting, link checks, and multi-version CI. | L |
| 6 | P1 | The repository is not legible to coding agents | No `AGENTS.md`, build/test commands, task conventions, data rules, security boundaries, or machine-verifiable acceptance criteria exist. | Add a vendor-neutral `AGENTS.md`, bounded task templates, deterministic tests, data manifests, and commands for setup, test, notebook execution, site build, and link validation. | S-M |
| 7 | P1 | Notebook presentation depends on obsolete frontend internals | Every notebook injects `styles/numericalmoocstyle.css`. It targets Classic Notebook DOM selectors, loads fonts over HTTP, calls MathJax 2 APIs, and includes HTML in a file named `.css`. Notebook 7 explicitly warns that classic customizations can break. | Recreate the visual identity in the new publication theme rather than patching the legacy CSS. Use supported, accessible, responsive styling and no executable per-notebook injection. | M |
| 8 | P1 | Licensing is internally inconsistent | Root `LICENSE` identifies instructional material as CC BY 3.0 while notebook banners identify CC BY 4.0; detailed asset provenance is incomplete. | Before migration, confirm which contributions and assets may be reused. Give the new repository a clear license and provenance model, add SPDX-style notices where practical, document third-party adaptations, and add `CITATION.cff`. Do not silently relicense contributions. | S-M |
| 9 | P1 | Onboarding is materially obsolete and too large for the new course | It mandates Python 3.4, uses Continuum URLs, hard-coded Anaconda paths, bash startup files on macOS, Red Hat/GW lab assumptions, Classic Notebook UI screenshots, and an outdated Git/GitHub authentication flow. | Do not refresh the legacy screenshots or reproduce the full module. Write a concise new-edition quick start with a hosted option, a locked local environment, and only essential notebook/Git review concepts. If a conda route is offered, recommend Miniconda rather than the full Anaconda distribution. | S-M |
| 10 | P1 | Accessibility has not been engineered | Of 75 statically referenced instructional images, 23 HTML `<img>` elements have no `alt`, and 6 Markdown alt labels are generic. GIFs/animations lack documented static equivalents or transcripts; embedded video caption status is not recorded. | Apply WCAG-oriented authoring checks to migrated and newly created materials: descriptive alternatives, captions/transcripts, keyboard/contrast checks, nonanimated equivalents, semantic headings, accessible published outputs, and automated checks supplemented by manual review. | L |
| 11 | P1 | Link rot and runtime network dependence create avoidable fragility | Of 158 HTTP(S) targets, 134 returned 2xx in the automated probe; 15 returned 404, 3 returned 403, 1 returned 520, and 5 timed out or failed SSL/connection checks. Some failures are anti-bot or punctuation false positives, but the Gray-Scott data URL fails at runtime despite the file being in the repository. | Make computation offline-first, use local/versioned data with checksums, update old HTTP/docs links, replace unstable personal-site copies with DOI/archival sources where legal, and run a scheduled link checker. | M |
| 12 | P1 | There are no explicit quality gates for numerical correctness | No `assert`, `pytest`, `unittest`, `doctest`, or NumPy testing use was found. Passing notebooks mostly show plots or values without machine-checked invariants or convergence thresholds. | Add unit, regression, property, invariant, and convergence tests. Test conservation, boundary conditions, exact/manufactured solutions, observed order, stability limits, and solver residuals. | L |
| 13 | P2 | The broader curriculum is fragmented | The notebook course focuses on ODE/PDE applications, and planned performance and BEM modules never reached `master`. | Decide the 2026 scope explicitly. Add a foundations module and a performance/production-solvers module before attempting every topic. Treat BEM and differentiable/GPU computing as advanced options. | L |
| 14 | P2 | Asset and metadata hygiene needs review | Notebook outputs include 78 embedded PNGs and one stored error; no cell has tags; 20 instructional assets appear unreferenced by basename; one image is duplicated exactly; data lacks a manifest; notebook filenames and kernel metadata are inconsistent. | During migration, normalize selected names and metadata, establish an output policy, tag expected errors/slow cells, and create a data manifest with provenance/checksums. Leave unused legacy assets in place rather than cleaning this repository. | M |
| 15 | P2 | Useful material is stranded on obsolete branches | `origin/performance_dev` contains three unmerged notebooks, including NumbaPro-era content; `origin/boundary_solution` contains a Green-function/BEM lesson and README. | Inventory intellectual content, salvage explanations/figures with attribution into the new repository, and rewrite code against current tools. Do not merge the branches wholesale. | S-M |
| 16 | P3 | Documentation polish is uneven | Root/module text contains typos and stale terminology (`OS X`, `implict`, `discretizign PDEx`, `PDS`, badge-era wording); module summaries do not always list every notebook. | Do not copy-edit the legacy edition. Correct and standardize only text selected for the new course. | S |

## Notebook reproducibility audit

These execution results are a diagnostic inventory for migration. They do not imply that all 26 legacy notebooks should be repaired in place or carried into the new edition.

### Collection-wide metadata

- All notebooks use nbformat 4 and parse successfully.
- 23 notebooks request `py36-mooc`; 3 request `py36-mae6286`.
- Recorded Python versions are 3.6.5 (7 notebooks), 3.6.6 (16), and 3.6.9 (3).
- All 386 code cells have saved execution counts.
- Saved outputs include 77 `execute_result`, 47 stream, 56 display, and 1 error output.
- There are no notebook attachments and no cell tags.
- Every notebook ends with legacy style loading through `IPython.core.display.HTML` and `../../styles/numericalmoocstyle.css`.

### Clean execution results

“Pass” means that the supplied notebook executed from top to bottom in the compatibility environment. It does not mean that an assignment solution exists or that every numerical claim has a test.

| Notebook | Result | New-edition migration note |
|---|:---:|---|
| `01_01_Phugoid_Theory.ipynb` | Fail | Four calls reach `phugoid.py`, whose `ax.axis(..., adjustable='box')` call is incompatible with current Matplotlib. |
| `01_02_Phugoid_Oscillation.ipynb` | Pass | Add numeric assertions for exact-solution error and observed order. |
| `01_03_PhugoidFullModel.ipynb` | Pass | Add convergence thresholds and separate the solver from narrative state. |
| `01_04_Second_Order_Methods.ipynb` | Pass | Strong comparison opportunity; convert plotted order claims to tests. |
| `Rocket_Assignment.ipynb` | Pass | Contains only one executable footer cell; pass status does not test a rocket solution. Needs starter API, rubric, tests, and reference behavior. |
| `02_01_1DConvection.ipynb` | Pass | Add conservation/translation/error tests and current array semantics. |
| `02_02_CFLCondition.ipynb` | Pass | Turn stability experiments into parameterized tests and an agent falsification task. |
| `02_03_1DDiffusion.ipynb` | Fail | `anim.to_html5_video()` requires unavailable `ffmpeg`; installation is described in prose but absent from the environment. |
| `02_04_1DBurgers.ipynb` | Fail | The intentional undefined `x` teaching cell is untagged; later animation also fails without `ffmpeg`. |
| `03_01_conservationLaw.ipynb` | Fail | Three animation cells require `ffmpeg`. Numerical cells continue when animation errors are allowed. |
| `03_02_convectionSchemes.ipynb` | Fail | Six animation cells require `ffmpeg`. This notebook is a good candidate for a tested scheme-comparison library. |
| `03_03_aBetterModel.ipynb` | Fail | `eq2 - 3 * eq3` is intended as a teaching demonstration, but modern SymPy raises `TypeError` rather than merely returning an unhelpful expression; a later animation also requires `ffmpeg`. |
| `03_04_MUSCL.ipynb` | Fail | Two animation cells require `ffmpeg`; add conservation, monotonicity/TVD, and benchmark tests. |
| `03_05_Sods_Shock_Tube.ipynb` | Pass | Assignment prompt has only one footer code cell; needs a solver interface, tests, rubric, and reference comparisons. |
| `04_00_Python_Function_Quirks.ipynb` | Pass | Material remains useful but should be reframed around pure functions, state, mutation, and agent-reviewable APIs. |
| `04_01_Heat_Equation_1D_Explicit.ipynb` | Pass | Add maximum-principle/stability and boundary-condition tests. |
| `04_02_Heat_Equation_1D_Implicit.ipynb` | Pass | Compare pedagogical dense construction with sparse production solvers. |
| `04_03_Heat_Equation_2D_Explicit.ipynb` | Fail | `pyplot.axis('scaled', adjustable='box')` is incompatible with current Matplotlib. |
| `04_04_Heat_Equation_2D_Implicit.ipynb` | Fail | Same Matplotlib failure; dense matrix strategy also deserves a scalability warning and sparse alternative. |
| `04_05_Crank-Nicolson.ipynb` | Pass | Executes in about 35 seconds in the probe; tag as slow and test claimed order with tolerances. |
| `04_06_Reaction_Diffusion.ipynb` | Fail | Downloads `uvinitial.npz` from an unstable GitHub HTML URL to the notebook directory even though `data/uvinitial.npz` is tracked. Downstream cells then fail when download fails. |
| `05_01_2D.Laplace.Equation.ipynb` | Pass | Add manufactured-solution and boundary-order tests. |
| `05_02_2D.Poisson.Equation.ipynb` | Pass | Add residual and iteration-budget assertions. |
| `05_03_Iterate.This.ipynb` | Pass | Takes about 94 seconds due in part to timing cells; Numba installation prose is stale. Mark slow/benchmark cells and isolate optional performance work. |
| `05_04_Conjugate.Gradient.ipynb` | Pass | Compare the pedagogical implementation with `scipy.sparse.linalg.cg`; test SPD preconditions and residual histories. |
| `05_05_Stokes.Flow.ipynb` | Pass | Only four code cells, mostly setup/footer; the assignment needs a defined API, tests, conservation/residual checks, and rubric. |

The continue-after-errors pass found no additional independent failure families. It did reveal the later `ffmpeg` failures in Burgers and the improved traffic model, plus expected downstream failures after the Gray-Scott data download.

### Python helper modules

The actions below apply only when a helper's concepts or code are selected for migration; the legacy copies should remain unchanged.

| File | Assessment |
|---|---|
| `lessons/01_phugoid/phugoid.py` | Clear docstrings and small functions. Update the Matplotlib aspect call, remove global `numpy.seterr(all='ignore')` in favor of a narrow context, return figure/data for testing instead of always showing, and add unit/regression tests. |
| `lessons/03_wave/traffic.py` | Small and readable. Add input validation/type hints/tests, clarify units, and decide behavior outside the hard-coded `x < 3.0` case. |
| `lessons/05_relax/helper.py` | Useful shared logic. Separate plotting from solvers, use modern 3D-axis construction, type/test the norm and Jacobi solver, return convergence status explicitly, and test stopping criteria. |
| `lessons/05_relax/multigrid_helper.py` | Currently unreferenced and not importable with Numba 0.60 because `numba.autojit` was removed. It lacks module documentation/tests and mutates caller arrays. Either rewrite it as a tested new-edition multigrid lesson or leave it behind; do not delete the legacy copy. |

## Documentation and content audit

### Top-level files

#### `README.md`

Strengths: concise history, clear open-education intent, and a readable model-based module map.

Leave the legacy README unchanged. It is evidence of how the original course was presented and should not be made to describe a course that now lives elsewhere. The new repository needs its own README with current status, prerequisites, learning outcomes, tested quick start, course sequence, license, agent-use policy, and links to its published site. Once the new edition is public, the organization-level repository description or other non-content metadata can distinguish the legacy and current repositories without rewriting this historical README.

#### `nm_python_env.yaml`

This file is historically useful but unsuitable as a current install route. Python 3.4 reached end of life in 2019 and Python 3.6 in 2021; the exact conda build pins and old OpenSSL, Qt 4, Notebook 3, and `jsanimation` dependencies belong to the legacy record.

Leave the file in place here. The new repository should define a canonical, lockable environment from current direct dependencies, account explicitly for any retained system tools such as `ffmpeg`, and test setup from a clean clone. If conda is offered to learners, use Miniconda as the lightweight installer—not the full Anaconda distribution—and keep the project environment isolated from `base`.

#### `styles/numericalmoocstyle.css`

The file mixes `<link>`, `<style>`, and `<script>` HTML with CSS. It targets `#notebook`, `.text_cell_render`, `.CodeMirror`, and other Classic Notebook internals; uses several HTTP font URLs; fixes desktop widths; and configures MathJax through the version-2 `MathJax.Hub` interface. Leave it unchanged as part of the legacy presentation. Use it only as a visual reference when creating supported, responsive, accessible theme CSS in the new repository.

#### `.gitignore`

The legacy ignore file is intentionally small. Any broader rules for tool caches, site output, or generated notebook artifacts belong in the new repository and should not hide lock files.

#### `LICENSE`

Do not silently alter the legacy license notices. Before copying material, establish what can be migrated from the CC BY 3.0 top-level material, CC BY 4.0 notebook banners, MIT-licensed code, data, and third-party media. State the new repository's license boundaries clearly and retain per-asset/source attribution.

### Getting started

The four-file legacy onboarding module should be retired, not refreshed. Its command-line detail, Red Hat/GW lab assumptions, full-Anaconda installation path, Classic Notebook screenshots, and password-era GitHub workflow are too specific to their original setting. Do not replace its screenshots or edit its instructions in place.

The new edition should have a short prerequisites and quick-start path rather than another general computing mini-course:

1. offer a zero-install hosted route where feasible;
2. provide one canonical locked local environment and a verification command;
3. if a conda workflow is offered, recommend Miniconda and an isolated course environment, never the full Anaconda distribution or changes learners do not understand to `PATH`;
4. link to maintained external shell, Jupyter, Git, and editor resources instead of duplicating their full documentation;
5. retain only course-specific concepts: choosing the correct kernel, restart-and-run-all, deterministic execution, locating files/data, running tests, reading diffs, and reviewing agent-generated changes;
6. include recovery steps, supported platforms, and a no-paid-tool path.

This reduces maintenance burden and keeps onboarding proportional to the numerical-methods learning goals.

### Module-by-module review

| Module | Keep | New-edition review/rewrite | 2026 agentic opportunity |
|---|---|---|---|
| 1: Phugoid | Physical motivation, exact versus numerical solution, Euler/RK comparison, convergence, paper-airplane/rocket context | Fix plotting, make units and APIs explicit, add tests and measurable objectives, modernize ODE-library comparison, add rocket rubric/reference cases | Have an agent implement two integrators from a written contract; students design convergence tests, find defects, and defend solver choice. |
| 2: Space and Time | Stencils, CFL/domain of dependence, diffusion, Burgers, vectorization, symbolic solution | Make deliberate-error cells executable in CI, remove codec fragility, update SymPy narrative, add conservation/stability tests | Ask agents to propose vectorizations and boundary implementations; students use invariants and manufactured solutions to reject subtly wrong variants. |
| 3: Riding the Wave | Conservation-law framing, traffic model, classical schemes, finite volume/MUSCL, Sod benchmark | Replace many repeated animation blocks, add production Riemann-solver context, clarify limiter/TVD claims, provide Sod tests and rubric | Run an “agent tournament” on shock-capturing schemes using hidden discontinuous cases, conservation, positivity, and error metrics; students review failure modes. |
| 4: Spreading Out | Boundary conditions, explicit/implicit contrast, 2D discretization, Crank-Nicolson, Gray-Scott | Use sparse matrices/solvers where scale demands, remove runtime download, test maximum principle/stability/order, modernize state/mutation lesson | Students give an agent a PDE/BC specification, then audit matrix assembly, boundary rows, units, residuals, and computational complexity. |
| 5: Relax | Jacobi/GS/SOR progression, performance motivation, CG geometry, Stokes assignment | Modernize/archive multigrid helper, separate benchmarks from correctness, compare with SciPy/optional PyAMG, state CG assumptions, build Stokes rubric/tests | Let agents optimize only after a correctness suite passes; students evaluate speed, memory, convergence, and whether optimizations preserve numerical behavior. |

### Assessment materials

Four assignment-oriented notebooks are present: Rocket, Sod, Reaction-Diffusion, and Stokes. A fifth assignment, Traffic, is described in the Module 2 documentation but is not represented by a distinct assignment notebook in the current tree. The GitHub materials do not contain a complete, current assessment system:

- assignment notebooks are mostly narrative prompts and setup rather than defined package interfaces;
- platform numeric questions and quizzes are gone;
- no grading rubrics, tests, solution strategy, feedback bank, or current submission instructions are present;
- no policy explains collaboration, reuse, or generative/agentic AI;
- badge descriptions describe an unavailable process.

For each assignment selected for the new edition, create a student-facing task specification and rubric. Keep instructor reference solutions and hidden tests in an appropriately controlled repository if needed, while publishing enough open tests and reference cases to support learning. Leave the old badge process behind unless a new issuer, criteria, evidence model, and privacy policy are established.

### Figures, GIFs, and data

All statically discovered local references resolve. Both NPZ files load successfully and contain finite arrays:

- `uvinitial.npz`: arrays `U` and `V`, each 192 x 192;
- `relaxation_schedules.npz`: 12 one-dimensional timing/convergence-series arrays.

In the new repository, add provenance, generation scripts where available, units/meaning, license, checksum, and expected shapes to a data manifest. A migrated Gray-Scott lesson should read its versioned local data rather than download a second copy at runtime. `relaxation_schedules.npz` appears unreferenced and should migrate only if selected content uses it.

The exact duplicate `lessons/02_spacetime/figures/FTBS_stencil.png` and `lessons/03_wave/figures/FTBS_stencil.png` can be deduplicated during migration if both copies would otherwise be carried forward.

Accessibility scanning found 23 HTML images without `alt` attributes and 6 generic Markdown alternatives. The remaining labels are not necessarily adequate descriptions. Animated GIFs and generated animations need captions and static/key-frame or data-table alternatives.

## External-link audit

The automated check made read-only requests to 158 unique targets found in Markdown, notebook source, Python, CSS, and YAML. Results were:

| Result | Count | Interpretation |
|---|---:|---|
| HTTP 200 | 132 | Reachable during the audit. |
| HTTP 206 | 2 | Reachable partial-content response. |
| HTTP 404 | 15 | Review required; includes true stale links, some GitHub anti-automation behavior, and a few punctuation-contaminated raw URL detections. |
| HTTP 403 | 3 | Access denied to the checker; not proof of deletion. |
| HTTP 520 | 1 | Upstream/proxy failure. |
| Timeout/SSL/connection failure | 5 | Manual replacement or archival review required. `localhost:8888` is instructional and not an external defect. |

For links selected for the new edition, high-value updates include the following; a wholesale repair of legacy links is not recommended.

- replace old NumPy documentation under `docs.scipy.org/doc/numpy` with current `numpy.org/doc` links;
- replace HTTP with HTTPS where supported, including fonts and nbviewer links;
- use DOI/publisher/archive links for papers rather than fragile departmental copies;
- repair or archive the NASA Helios, Colorado-hosted Lighthill PDF, old Git teaching source, and example-repository references that returned 404;
- replace `pypi.python.org` and `numba-doc/dev` links with current stable documentation;
- use `raw.githubusercontent.com` only when an external raw file is truly necessary, with a pinned commit and checksum; local course data is preferable;
- periodically verify embedded YouTube availability and caption quality;
- use relative repository links in README/module indexes so branch-name and host rendering changes do not break navigation.

Do not treat an automated status alone as a deletion decision. Some publishers deny automated requests, and the main GitHub repository was manually confirmed accessible despite some `blob/master` requests returning 404 to the checker.

## Proposed 2026 course model

### Reframed course promise

> Learn to formulate, implement, verify, and communicate numerical solutions for engineering models—working both directly in scientific Python and through supervised coding agents.

The central educational claim should be that numerical judgment becomes more important, not less, when code generation is cheap. Students need to know what problem was solved, whether it was the intended problem, what errors dominate, what evidence supports the result, what an agent changed, and what remains uncertain.

### Proposed learning outcomes

By the end of the course, a learner should be able to:

1. translate an engineering model into variables, equations, units, initial/boundary conditions, assumptions, and success criteria;
2. choose and justify a numerical method using accuracy, stability, conservation, conditioning, cost, and implementation constraints;
3. write an agent-ready computational task specification with explicit inputs, outputs, invariants, tolerances, and prohibited behavior;
4. implement core methods directly well enough to understand their failure modes;
5. supervise an agent that implements, refactors, tests, or optimizes numerical software;
6. inspect code and diffs for indexing, sign, units, boundary, shape, state, precision, and complexity errors;
7. verify results with exact or manufactured solutions, refinement studies, residuals, conservation laws, limiting cases, and independent implementations;
8. distinguish discretization, iteration, roundoff, modeling, data, and agent-induced errors;
9. produce a reproducible computational artifact with pinned dependencies, tests, provenance, and a clear report;
10. manage tool/data permissions and explain privacy, security, attribution, and accountability when an agent acts on external systems;
11. compare pedagogical implementations with production scientific libraries and justify when to use each;
12. communicate conclusions and uncertainty to an engineering audience and defend the evidence orally or in review.

### Learning cycle for every module

Use a repeated six-stage workflow:

1. **Model:** derive or interpret the governing model and units.
2. **Specify:** write numerical and software acceptance criteria before implementation.
3. **Implement/delegate:** code a core component directly and delegate a bounded component to an agent.
4. **Inspect:** review the implementation, diff, dependencies, and tool actions.
5. **Verify and validate:** run invariant, convergence, benchmark, and sensitivity tests.
6. **Communicate:** report method, evidence, limitations, provenance, and unresolved risks.

This keeps AI use tied to numerical-method learning rather than adding a detached “prompt engineering” lecture.

### Agent-use and assessment policy

Use a transparent, outcome-based policy instead of trying to detect AI-generated prose or code.

| Activity | Suggested agent policy | Evidence assessed |
|---|---|---|
| Foundational concept checks | Individual, closed-resource or tightly specified aids | Method selection, stability/error reasoning, units, interpretation. |
| Guided labs | Agents allowed and encouraged | Task specification, review notes, tests, corrected defects, short reflection. |
| Coding assignments | Agents allowed within declared boundaries | Working artifact, test quality, convergence/physics evidence, provenance, engineering decisions. |
| Debugging/review practical | Agent supplies a plausible flawed solution or student reviews an agent diff | Defects found, severity, minimal reproduction, corrected test, explanation. |
| Oral/code defense | Agent unavailable during a short defense | Ownership of assumptions, implementation, plots, limitations, and next experiment. |
| Team project | Agents treated as tools, not team members | Human responsibility map, review approvals, risk log, reproducible release. |

Require a lightweight `AI_USAGE.md` or report section recording:

- tools/models used and dates;
- tasks delegated;
- important prompts/specifications or links to a machine-readable log;
- files/actions the agent was allowed to access;
- material suggestions accepted, rejected, or corrected;
- verification performed by the learner;
- external sources and generated assets requiring attribution.

Do not grade verbosity of prompt logs. Grade whether the learner established trustworthy evidence. Provide a no-paid-tool path and avoid a policy tied to one vendor.

### Agent safety and engineering responsibility

Agent exercises should begin with local, sandboxed files and synthetic/public data. Network access, secrets, cloud resources, or costly compute should require explicit human approval and bounded quotas. Teach that tool descriptions and generated outputs are untrusted until verified. This aligns with the consent, control, privacy, and tool-safety principles in the current Model Context Protocol specification and the evaluation/risk-management emphasis of the NIST Generative AI Profile.

## Proposed new-edition repository architecture

One possible layout for the fresh repository is:

```text
.
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── CITATION.cff
├── LICENSES/
├── pyproject.toml
├── <one canonical lock file>
├── .github/workflows/
│   ├── test.yml
│   ├── notebooks.yml
│   ├── book.yml
│   └── links.yml
├── src/numerical_mooc/
│   ├── ode/
│   ├── transport/
│   ├── diffusion/
│   └── elliptic/
├── tests/
│   ├── unit/
│   ├── convergence/
│   ├── regression/
│   └── notebooks/
├── book/
│   ├── myst.yml
│   ├── index.md
│   ├── quickstart.md
│   └── modules/
├── assignments/
│   ├── student/
│   ├── public_tests/
│   └── rubrics/
└── data/
    ├── README.md
    ├── checksums.txt
    └── ...
```

Key design decisions:

- **Notebooks remain first-class course pages**, but reusable numerical logic lives in importable modules with small, explicit APIs.
- **One canonical environment** must install locally and in CI. Use a lock-capable tool appropriate to both Python and any retained system dependencies; document export formats as secondary, not competing sources of truth.
- **Python 3.13 is the recommended floor**, with CI on 3.13 and 3.14. Do not target the 3.15 prerelease for a course launch.
- **NumPy 2.x compatibility is required.** The official migration guide documents namespace and API removals; CI should prevent a repeat of decade-long dependency drift.
- **Animations are build artifacts**, not prerequisites for numerical correctness. Either include `ffmpeg` deterministically or use a supported browser-native/static fallback.
- **Data is offline-first and immutable.** Runtime downloads must be pinned, checksummed, cached, and optional.
- **Jupyter Book 2/MyST is the publication layer.** It supports executable notebooks, cross-references, math, websites, and PDF output without embedding frontend code in every notebook.
- **`AGENTS.md` is concise and operational.** It should list setup, tests, style, numerical tolerances, slow-test policy, data/network rules, and security constraints. The open format is intended as a README-like guide for coding agents.

## Verification and CI design

At minimum, every pull request should run:

1. environment installation from the lock file;
2. formatting/linting and import checks;
3. unit tests for solver/model functions;
4. fast numerical invariant and regression tests;
5. selected convergence tests with robust tolerances;
6. fresh-kernel notebook execution;
7. Jupyter Book build;
8. internal-link and scheduled external-link checks;
9. accessibility/static HTML checks;
10. data checksum/provenance validation.

Slow benchmarks and high-resolution convergence studies should run on a schedule or explicit label, not block every edit. Store benchmark trends as artifacts and avoid brittle exact timing assertions.

Useful numerical test categories include:

- exact and manufactured solutions;
- zero-source/constant-state/steady-state limiting cases;
- conservation of mass or flux balance;
- positivity, bounds, and maximum principles where applicable;
- boundary-condition residuals;
- observed order of accuracy over multiple refinements;
- iteration residual reduction and termination reason;
- agreement between loop and vectorized implementations;
- agreement with trusted SciPy solvers at stated tolerances;
- seeded randomized/property tests for shapes and parameter ranges;
- negative tests that prove unstable or invalid configurations are detected.

`nbval` can rerun notebooks and compare stored outputs, while its lax mode can focus on execution failures. Use it selectively: image, timing, warning, and floating-point output can be brittle. Prefer assertions in package tests and use notebook execution primarily to prove that the narrative remains runnable.

## Phased modernization plan

### Phase 0: freeze and charter (1 week)

1. Record that this repository is the legacy edition; do not use it as the development base for 2026.
2. Optionally tag the audited state without rewriting history or revising legacy teaching materials.
3. Choose the new repository name and establish its ownership, branch protection, contribution process, and relationship to this repository.
4. Resolve the license and contribution authority for material selected for migration.
5. Decide the initial audience, prerequisites, scope, delivery platform, and assessment model.
6. Create a migration manifest that classifies each legacy module or asset as migrate, rewrite, reference, or leave behind.

**Exit gate:** a new-repository charter, license decision path, migration manifest, and prioritized issue board.

### Phase 1: scaffold and prove one vertical slice (2-3 weeks)

1. Create the fresh repository under the same organization.
2. Add its supported Python 3.13/3.14, NumPy 2.x environment and lock it.
3. Establish package, test, notebook/book, data, assignment, and CI structure.
4. Port Module 1 selectively, separating reusable solver code from narrative notebooks.
5. Rewrite migrated content for clean kernels, current APIs, explicit numerical tests, accessible presentation, and offline data.
6. Add the concise quick start; make Miniconda an optional lightweight local route, not a required full distribution.
7. Publish a preview site from CI.

**Exit gate:** a fresh clone of the new repository can set up, test, execute, and publish the Module 1 vertical slice with one documented workflow.

### Phase 2: migrate the core course (3-5 weeks)

1. Selectively port the strongest Module 2-5 narratives and examples.
2. Rewrite reusable solver/model modules and add numerical tests as content is migrated.
3. Build coherent site navigation and syllabus-aligned module pages in the new repository.
4. Restore selected assignments with public tests, rubrics, reference behavior, and feedback.
5. Complete attribution, data, link, and accessibility work for migrated material.
6. Leave obsolete onboarding, unused assets, platform-specific text, and unselected notebooks in the legacy repository.

**Exit gate:** every selected page is reachable from the new course map; CI is green; a new learner can start without instructor intervention; accessibility review has documented results.

### Phase 3: pilot the agentic redesign (4-6 weeks)

Start with two modules rather than rewriting everything:

- **Module 1 pilot:** agent implements or refactors integrators from a contract; learner owns convergence evidence and review.
- **Module 4 or 5 pilot:** agent assembles/optimizes a PDE solver; learner audits boundary conditions, sparse structure, residuals, and performance.

Create the AI-use policy, task specification template, provenance format, flawed-agent review practical, and oral-defense rubric. Run the pilot with learners, collect time/error/fairness data, and revise.

**Exit gate:** assessments distinguish numerical understanding from code-generation fluency, work with at least two agent/tool options or a no-agent route, and produce auditable evidence.

### Phase 4: expand the curriculum (later releases)

In priority order:

1. foundations: floating-point/error, conditioning, and linear/nonlinear solvers;
2. production sparse solvers, preconditioning, profiling, and performance portability;
3. uncertainty, sensitivity, reproducibility, and data provenance;
4. optional GPU/array-backend and automatic-differentiation labs;
5. optional BEM or multigrid material recovered conceptually from dormant branches.

Avoid making a fast-changing agent API or GPU framework a hard dependency for the core course. Teach stable interfaces, evidence, and engineering controls.

## First issue set

Create these issues in the new-edition repository, in order:

1. **Charter/migration:** define scope, ownership, repository relationship, and the migrate/rewrite/reference/leave-behind manifest.
2. **Legal/provenance:** reconcile license boundaries for selected material and inventory third-party media.
3. **Environment:** create the Python 3.13/3.14 + NumPy 2.x locked environment and optional Miniconda setup route.
4. **Architecture:** scaffold `src/`, tests, book, assignments, data, and CI around a Module 1 vertical slice.
5. **CI:** execute required notebooks from clean kernels and run numerical acceptance tests.
6. **Migration compatibility:** port selected content while resolving current Matplotlib, SymPy, animation, data, and helper-code issues.
7. **Publication:** build minimal Jupyter Book 2 navigation and preview deployment.
8. **Onboarding:** write the concise quick start, environment verification, and maintained-resource links.
9. **Assessment:** restore the Rocket task with rubric/public tests and pilot the agent-use evidence format.
10. **Accessibility:** add image alternatives, animation fallbacks, captions, and theme contrast/keyboard review for migrated content and generated outputs.
11. **Links/data:** migrate only needed links/data and add manifests/checksums.
12. **Agent guidance:** add `AGENTS.md` after the real build/test commands exist.

## Definition of done for a 2026 release

A release in the new-edition repository is ready when:

- a fresh clone runs from one documented setup command on supported systems;
- all required notebooks execute offline from a fresh kernel in CI;
- all package tests and numerical acceptance tests pass on Python 3.13 and 3.14;
- the course site builds without broken internal links;
- runtime data has provenance and checksums;
- no unexpected exception output is committed;
- assignments have learning outcomes, rubrics, public tests, and submission/evidence instructions;
- the agent-use policy and no-paid-tool access path are published;
- each agent-enabled assignment requires specification, review, verification, and provenance evidence;
- image alternatives, captions/transcripts, animation fallbacks, keyboard access, contrast, and generated PDF accessibility have been reviewed;
- instructional/software/data licenses and third-party attributions are consistent and visible;
- CI/build/test/security instructions are documented for humans and agents;
- an academic owner and technical maintainer have agreed to a dependency/link review cadence.

## Candidate legacy assets for migration review

The following 20 instructional files had no reference found by exact basename in decoded Markdown, notebook source, Python, CSS, or YAML. Review them only when selecting material for the new edition. This is not a cleanup or deletion list; unselected files should remain in the legacy repository.

- `lessons/01_phugoid/figures/glider_forces_nodrag.png`
- `lessons/01_phugoid/figures/rocket_CV.png`
- `lessons/02_spacetime/figures/stencil-1.png`
- `lessons/02_spacetime/figures/stencil-2.png`
- `lessons/02_spacetime/figures/stencil-3.png`
- `lessons/02_spacetime/figures/stencil-4.png`
- `lessons/02_spacetime/figures/vectorizedstencil.svg`
- `lessons/03_wave/figures/finite_volume.svg`
- `lessons/03_wave/figures/linear_extrapolation.png`
- `lessons/03_wave/figures/linear_extrapolation.svg`
- `lessons/03_wave/figures/linear_reconstruction.png`
- `lessons/03_wave/figures/linear_reconstruction.svg`
- `lessons/03_wave/figures/pipe1.png`
- `lessons/03_wave/figures/pipe1.svg`
- `lessons/04_spreadout/figures/2dgrid_indices.svg`
- `lessons/04_spreadout/figures/btcs_stencil.png`
- `lessons/04_spreadout/figures/implicit_formula.png`
- `lessons/04_spreadout/figures/implicit_matrix.svg`
- `lessons/05_relax/data/relaxation_schedules.npz`
- `lessons/00_getting_started/images/condainstall.gif`

## Current primary references for the modernization

- [Python version status](https://devguide.python.org/versions/) — confirms support status and end-of-life dates for the Python versions involved.
- [NumPy 2.0 migration guide](https://numpy.org/doc/2.0/numpy_2_0_migration_guide.html) and [current NumPy documentation](https://numpy.org/doc/) — basis for a NumPy 2.x review rather than assuming 1.x compatibility.
- [Jupyter Notebook 7 migration guide](https://jupyter-notebook.readthedocs.io/en/stable/migrate_to_notebook7.html) — documents incompatibility risk for Classic Notebook extensions and customizations.
- [Jupyter Book 2 documentation](https://jupyterbook.org/latest/) — current executable publication route for notebooks and MyST content.
- [GitHub Actions: building and testing Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) — current CI patterns and explicit Python-version setup.
- [nbval documentation](https://nbval.readthedocs.io/en/latest/) — notebook execution/output validation options.
- [AGENTS.md open format](https://agents.md/) — vendor-neutral repository guidance for coding agents.
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-11-25) — current tool/context protocol and explicit consent, privacy, and tool-safety principles.
- [NIST AI RMF Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) — risk, trustworthiness, measurement, and evaluation frame for agent-enabled work.

## Bottom line

Preserve the course’s identity: real engineering models, numerical experiments, convergence, stability, conservation, and clear exposition. Preserve this repository as the legacy record. Build the 2026 edition separately as a reproducible, tested software project and executable course site in which students learn to supervise computational agents by producing stronger specifications and stronger evidence than an agent can produce unaided.
