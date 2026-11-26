from typing import List, Dict, Any

class PresentationDeckGenerator:
    """
    Generates presentation slides with diverse, creative, academic layouts:
    - 'hero_split': High-impact definition banner + 2 deep-dive columns
    - 'pipeline': Horizontal progressive 3-stage or 4-stage pipeline workflow
    - 'worked_example': Problem statement slate + progressive steps + solution box
    - 'comparison': Side-by-side comparative analysis board
    - 'traps_dashboard': High-yield exam warning alert cards & NAT shortcuts
    - 'cards': Multi-pillar structured concept cards
    """

    C_GREEN = "#2E6B4B"
    C_RUST = "#C25E38"
    C_TEAL = "#2A6F72"
    C_ORANGE = "#D96B27"
    C_BLUE = "#1D4ED8"
    C_PURPLE = "#6D28D9"
    C_RED = "#B91C1C"

    DECKS = {
        # ==========================================
        # PROBABILITY & STATISTICS
        # ==========================================
        "Sample space and events": [
            {
                "layout": "hero_split",
                "part": "PART 1 • FOUNDATIONS",
                "title": "Sample Space, Events & Probability Space",
                "subtitle": "How uncertainty is mathematically modeled in GATE Data Science & AI",
                "hero": {
                    "badge": "MATHEMATICAL DEFINITION",
                    "text": "A <b>Probability Space</b> is a formal measure-theoretic triple <b>(Ω, 𝓕, P)</b> where <b>Ω</b> is the sample space of all outcomes, <b>𝓕</b> is a σ-algebra of valid events, and <b>P</b> is a real-valued probability measure assigning likelihoods P(A) ∈ [0, 1]."
                },
                "left_card": {
                    "header": "Sample Space (Ω) & Outcomes",
                    "color": C_GREEN,
                    "body": "• <b>Sample Space (Ω):</b> Set of all possible outcomes of a random experiment.<br>• <b>Outcome (ω):</b> A single elementary result (ω ∈ Ω).<br>• <i>Discrete Example:</i> Tossing two fair dice gives |Ω| = 6 × 6 = 36 ordered pairs.<br>• <i>Continuous Example:</i> Life of an electronic component: Ω = [0, ∞) seconds."
                },
                "right_card": {
                    "header": "Events (A ⊆ Ω) & σ-Algebra",
                    "color": C_RUST,
                    "body": "• <b>Event (A):</b> Any valid subset of outcomes (A ⊆ Ω).<br>• The event occurs if the experimental outcome ω ∈ A.<br>• <b>Null Event (∅):</b> Impossible event; P(∅) = 0.<br>• <b>Certain Event (Ω):</b> Guaranteed event; P(Ω) = 1.<br>• For discrete spaces, 𝓕 is simply the power set 2^Ω."
                },
                "summary": "Every probabilistic model in GATE begins by defining Ω and formulating events as subsets.",
                "footer": "Source: Mathematics for Machine Learning (mml-book.pdf), Section 6.1 (Page 181)"
            },
            {
                "layout": "cards",
                "part": "PART 2 • KOLMOGOROV AXIOMS",
                "title": "The Three Axioms of Probability",
                "subtitle": "Non-negotiable foundational laws governing all probabilistic reasoning",
                "columns": [
                    {
                        "header": "1. Non-Negativity",
                        "color": C_GREEN,
                        "body": "P(A) ≥ 0 for all A ∈ 𝓕.<br>Probabilities can never be negative under any physical or mathematical circumstance."
                    },
                    {
                        "header": "2. Total Certainty",
                        "color": C_RUST,
                        "body": "P(Ω) = 1.<br>The total probability of the entire sample space equals unity (100% certainty that something occurs)."
                    },
                    {
                        "header": "3. Countable Additivity",
                        "color": C_TEAL,
                        "body": "If A₁, A₂, ... are pairwise disjoint (Aᵢ ∩ Aⱼ = ∅ for i ≠ j):<br>P(⋃ Aᵢ) = ∑ P(Aᵢ)."
                    },
                    {
                        "header": "Corollaries",
                        "color": C_ORANGE,
                        "body": "• P(Aᶜ) = 1 - P(A)<br>• P(A ∪ B) = P(A) + P(B) - P(A ∩ B)<br>• P(∅) = 0<br>• If A ⊆ B, then P(A) ≤ P(B)."
                    }
                ],
                "summary": "Countable additivity applies strictly when sets share zero overlap.",
                "footer": "Source: mml-book.pdf, Chapter 6 (Page 182)"
            },
            {
                "layout": "comparison",
                "part": "PART 3 • CRUCIAL DISTINCTION",
                "title": "Mutually Exclusive vs. Independent Events",
                "subtitle": "The most frequent multiple-choice conceptual trap in GATE papers",
                "left": {
                    "badge": "MUTUALLY EXCLUSIVE (DISJOINT)",
                    "color": C_BLUE,
                    "points": [
                        "<b>Definition:</b> Events cannot happen simultaneously (A ∩ B = ∅).",
                        "<b>Intersection:</b> P(A ∩ B) = 0.",
                        "<b>Union Formula:</b> P(A ∪ B) = P(A) + P(B).",
                        "<b>Independence Status:</b> If P(A), P(B) > 0, they are <b>NEVER INDEPENDENT</b>! Knowing A occurred guarantees B did NOT occur."
                    ]
                },
                "right": {
                    "badge": "STATISTICALLY INDEPENDENT",
                    "color": C_PURPLE,
                    "points": [
                        "<b>Definition:</b> Occurrence of one event gives zero information about the other.",
                        "<b>Product Rule:</b> P(A ∩ B) = P(A) · P(B).",
                        "<b>Conditional:</b> P(A|B) = P(A) and P(B|A) = P(B).",
                        "<b>Exclusivity Status:</b> Can only be disjoint if P(A) = 0 or P(B) = 0."
                    ]
                },
                "summary": "Golden GATE Rule: Mutually exclusive events with positive probabilities are ALWAYS dependent!",
                "footer": "Source: GATE Examination Syllabus Reference & mml-book.pdf"
            },
            {
                "layout": "worked_example",
                "part": "PART 4 • WORKED GATE PROBLEM",
                "title": "Two-Dice Independence Walkthrough",
                "subtitle": "Step-by-step problem breakdown from official previous year exam papers",
                "problem": "A fair 6-sided die is rolled twice. Let event A = 'Sum of dice is 7' and event B = 'First die shows 3'. Compute P(A), P(B), P(A ∩ B), and test whether events A and B are independent.",
                "steps": [
                    {"step_num": "Step 1: Sample Space", "text": "Total outcomes |Ω| = 6 × 6 = 36 equiprobable ordered pairs (i, j). Favorable for A: {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)} → |A| = 6. Thus P(A) = 6/36 = 1/6."},
                    {"step_num": "Step 2: Event B & Intersection", "text": "Favorable for B: {(3,1), (3,2), (3,3), (3,4), (3,5), (3,6)} → |B| = 6. Thus P(B) = 6/36 = 1/6. The intersection A ∩ B requires first roll is 3 AND sum is 7: A ∩ B = {(3,4)} (exactly 1 outcome). Thus P(A ∩ B) = 1/36."},
                    {"step_num": "Step 3: Verification", "text": "Compute P(A) · P(B) = (1/6) × (1/6) = 1/36. Since P(A ∩ B) = 1/36 = P(A) · P(B), events A and B are strictly INDEPENDENT."}
                ],
                "answer": "✅ P(A) = 1/6, P(B) = 1/6, P(A ∩ B) = 1/36. Events A and B are STATISTICALLY INDEPENDENT.",
                "summary": "Always count favorable outcomes systematically using coordinate pairs.",
                "footer": "Source: Official GATE Sample Paper (DA Paper)"
            },
            {
                "layout": "traps_dashboard",
                "part": "PART 5 • EXAM TRAPS & NAT TIPS",
                "title": "Frequent GATE Traps & Quick Revision",
                "subtitle": "Mistakes that cost marks in GATE Data Science & AI",
                "traps": [
                    {"icon": "⚠️", "title": "Trap 1: Union vs Sum Overlap", "color": C_RED, "desc": "P(A ∪ B) ≠ P(A) + P(B) unless disjoint! Always subtract intersection: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)."},
                    {"icon": "⚠️", "title": "Trap 2: Continuous Zero Probability", "color": C_ORANGE, "desc": "For a continuous variable, P(X = c) = 0 for any single point c, yet the point is NOT impossible. Probabilities are strictly defined over intervals."},
                    {"icon": "💡", "title": "NAT Speed Trick: Boole's Bound", "color": C_BLUE, "desc": "Union bound: P(⋃ Aᵢ) ≤ ∑ P(Aᵢ). Use this to quickly calculate tight upper bounds in machine learning risk MCQs."}
                ],
                "summary": "Double-check for overlap whenever calculating unions in Numerical Answer Type (NAT) questions.",
                "footer": "Source: GATE Preparation Guidelines"
            }
        ],

        "Bayes Theorem": [
            {
                "layout": "pipeline",
                "part": "PART 1 • INFERENCE PIPELINE",
                "title": "The Bayesian Inference Pipeline",
                "subtitle": "A sequential 3-stage architecture for updating beliefs with evidence",
                "stages": [
                    {
                        "step": "STAGE 1",
                        "title": "Prior P(θ)",
                        "color": C_BLUE,
                        "desc": "Initial degree of belief in hypothesis θ before seeing any data. Encodes domain knowledge or population baseline prevalence."
                    },
                    {
                        "step": "STAGE 2",
                        "title": "Likelihood P(D | θ)",
                        "color": C_ORANGE,
                        "desc": "Probability of observing the dataset D given hypothesis θ. Evaluated using the forward generative model."
                    },
                    {
                        "step": "STAGE 3",
                        "title": "Posterior P(θ | D)",
                        "color": C_GREEN,
                        "desc": "Updated belief in θ given evidence D:<br><b>P(θ|D) = [P(D|θ) · P(θ)] / P(D)</b><br>Normalized by Total Evidence P(D)."
                    }
                ],
                "summary": "Posterior probability is proportional to Likelihood times Prior, normalized by Evidence.",
                "footer": "Source: Mathematics for Machine Learning (mml-book.pdf), Section 6.3 (Page 185)"
            },
            {
                "layout": "comparison",
                "part": "PART 2 • MACHINE LEARNING CONNECTION",
                "title": "MLE vs. MAP Estimation in AI",
                "subtitle": "How Bayes Theorem connects to regularization in Machine Learning",
                "left": {
                    "badge": "MAXIMUM LIKELIHOOD ESTIMATION (MLE)",
                    "color": C_BLUE,
                    "points": [
                        "<b>Formula:</b> θ_MLE = argmax_θ P(D | θ).",
                        "<b>Philosophy:</b> Fits data without considering prior beliefs.",
                        "<b>Risk:</b> Prone to severe overfitting when data samples are limited.",
                        "<b>Equivalence:</b> Equivalent to MAP with a uniform, uninformative prior."
                    ]
                },
                "right": {
                    "badge": "MAXIMUM A POSTERIORI (MAP)",
                    "color": C_PURPLE,
                    "points": [
                        "<b>Formula:</b> θ_MAP = argmax_θ [P(D | θ) · P(θ)].",
                        "<b>Philosophy:</b> Injects prior regularizing constraints on weights.",
                        "<b>L2 Equivalence:</b> Gaussian prior on weights θ ~ N(0, σ²I) ≡ <b>Ridge Regression (L2)</b>.",
                        "<b>L1 Equivalence:</b> Laplace prior on weights ≡ <b>Lasso Regression (L1)</b>."
                    ]
                },
                "summary": "Regularization in machine learning is simply MAP estimation under specific prior distributions.",
                "footer": "Source: mml-book.pdf, Chapter 9 (Page 290)"
            },
            {
                "layout": "worked_example",
                "part": "PART 3 • SOLVED GATE SCENARIO",
                "title": "Medical Diagnosis Problem Walkthrough",
                "subtitle": "Classic GATE Bayes theorem calculation with high false-positive rates",
                "problem": "A rare disease affects 1% of a population: P(D) = 0.01. A medical test has 95% sensitivity: P(+|D) = 0.95, and 90% specificity: P(-|H) = 0.90. A randomly selected person tests positive (+). Compute the true probability that the person has the disease: P(D|+).",
                "steps": [
                    {"step_num": "Step 1: Complementary Probabilities", "text": "Healthy population: P(H) = 1 - 0.01 = 0.99. False positive rate: P(+|H) = 1 - P(-|H) = 1 - 0.90 = 0.10 (10% of healthy test positive)."},
                    {"step_num": "Step 2: Law of Total Probability", "text": "Compute total evidence P(+): P(+) = P(+|D)P(D) + P(+|H)P(H) = (0.95 × 0.01) + (0.10 × 0.99) = 0.0095 + 0.0990 = 0.1085."},
                    {"step_num": "Step 3: Bayes' Formula", "text": "P(D|+) = [P(+|D) · P(D)] / P(+) = 0.0095 / 0.1085 ≈ 0.087557 (approx 8.76%)."}
                ],
                "answer": "✅ P(D | +) ≈ 0.0876 (only ~8.76% probability despite 95% test accuracy!).",
                "summary": "When disease prevalence is very low, the vast majority of positive tests are false positives.",
                "footer": "Source: Official GATE Sample Paper"
            },
            {
                "layout": "traps_dashboard",
                "part": "PART 4 • EXAM TRAPS",
                "title": "Bayes Calculation Traps in GATE",
                "subtitle": "Common mistakes in Numerical Answer Type (NAT) questions",
                "traps": [
                    {"icon": "⚠️", "title": "Missing Healthy False-Positives", "color": C_RED, "desc": "The #1 student error: forgetting the healthy group in the denominator. Always expand P(B) = P(B|A)P(A) + P(B|Aᶜ)P(Aᶜ)."},
                    {"icon": "💡", "title": "Odds Form Shortcut", "color": C_BLUE, "desc": "Posterior Odds = Prior Odds × Likelihood Ratio = (0.01/0.99) × (0.95/0.10). Speeds up MCQs by 50%!"},
                    {"icon": "⚠️", "title": "Intermediate Rounding Loss", "color": C_ORANGE, "desc": "In NAT questions, rounding intermediate denominators causes catastrophic precision loss. Keep 4 decimal places until the final answer."}
                ],
                "summary": "Always write out the law of total probability before substituting numerical values.",
                "footer": "Source: GATE Revision Notes"
            }
        ],

        # ==========================================
        # CALCULUS & OPTIMIZATION
        # ==========================================
        "Gradient descent": [
            {
                "layout": "hero_split",
                "part": "PART 1 • THEORETICAL FOUNDATION",
                "title": "The Gradient Vector & Directional Derivative",
                "subtitle": "Direction of steepest ascent and geometric contour properties",
                "hero": {
                    "badge": "GRADIENT VECTOR DEFINITION",
                    "text": "For a scalar-valued function f: ℝⁿ → ℝ, the **Gradient Vector** ∇f(x) is the vector of all first-order partial derivatives:<br><b>∇f(x) = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ</b><br>It points in the direction of maximum rate of increase (steepest ascent)."
                },
                "left_card": {
                    "header": "Geometric Properties",
                    "color": C_BLUE,
                    "body": "• <b>Orthogonal to Level Curves:</b> ∇f(x₀) is strictly perpendicular (normal) to the contour curve or level surface f(x) = c passing through x₀.<br>• <b>Magnitude ||∇f||:</b> Equals the maximum possible directional derivative at that point.<br>• <b>Steepest Descent:</b> -∇f(x) points in the direction of steepest rate of decrease."
                },
                "right_card": {
                    "header": "Directional Derivative Connection",
                    "color": C_PURPLE,
                    "body": "• The directional derivative along unit vector u (||u|| = 1) is:<br><b>D_u f(x) = ∇f(x) · u = ||∇f|| ||u|| cos θ</b>.<br>• Maximum when u is aligned with ∇f (θ = 0, cos 0 = 1).<br>• Zero when u is tangential to the level curve (θ = 90°)."
                },
                "summary": "The gradient vector is always perpendicular to level contours and points along steepest ascent.",
                "footer": "Source: Mathematics for Machine Learning (mml-book.pdf), Section 5.1 & 5.2"
            },
            {
                "layout": "worked_example",
                "part": "PART 2 • WORKED PROBLEM",
                "title": "Calculating Gradient & Directional Derivative",
                "subtitle": "Standard 2-mark GATE Calculus problem",
                "problem": "Given the scalar field f(x, y) = 3x²y - 2y³ + 5x, compute the gradient vector ∇f(x, y), evaluate ∇f at point P(1, 2), and find the maximum rate of increase at P.",
                "steps": [
                    {"step_num": "Step 1: Compute Partial Derivatives", "text": "∂f/∂x = d/dx[3x²y - 2y³ + 5x] = 6xy + 5.<br>∂f/∂y = d/dy[3x²y - 2y³ + 5x] = 3x² - 6y²."},
                    {"step_num": "Step 2: Assemble Gradient & Evaluate at P(1, 2)", "text": "∇f(x, y) = [6xy + 5, 3x² - 6y²]ᵀ.<br>At (1, 2): ∂f/∂x = 6(1)(2) + 5 = 17.<br>∂f/∂y = 3(1)² - 6(2)² = 3 - 24 = -21.<br>∇f(1, 2) = [17, -21]ᵀ."},
                    {"step_num": "Step 3: Maximum Rate of Increase", "text": "Maximum rate of increase is the Euclidean norm ||∇f(1, 2)||:<br>||∇f(1, 2)|| = √(17² + (-21)²) = √(289 + 441) = √730 ≈ 27.018."}
                ],
                "answer": "✅ ∇f(1, 2) = [17, -21]ᵀ, Maximum Rate of Increase = √730 ≈ 27.02.",
                "summary": "Always normalize the direction vector u when computing directional derivatives D_u f = ∇f · u.",
                "footer": "Source: GATE Examination Engineering Mathematics Past Papers"
            },
            {
                "layout": "comparison",
                "part": "PART 3 • OPTIMIZATION UPDATES",
                "title": "Gradient Descent vs. Newton-Raphson",
                "subtitle": "First-order vs. second-order optimization in Machine Learning",
                "left": {
                    "badge": "GRADIENT DESCENT (FIRST-ORDER)",
                    "color": C_BLUE,
                    "points": [
                        "<b>Update Rule:</b> x^(t+1) = x^(t) - γ ∇f(x^(t)).",
                        "<b>Information Used:</b> Only first derivatives (gradient).",
                        "<b>Per-Iteration Cost:</b> O(n) cheap operations.",
                        "<b>Sensitivity:</b> Highly sensitive to learning rate γ. Can oscillate in narrow valleys."
                    ]
                },
                "right": {
                    "badge": "NEWTON'S METHOD (SECOND-ORDER)",
                    "color": C_PURPLE,
                    "points": [
                        "<b>Update Rule:</b> x^(t+1) = x^(t) - [H(x^(t))]⁻¹ ∇f(x^(t)).",
                        "<b>Information Used:</b> Gradient and Hessian curvature matrix H.",
                        "<b>Per-Iteration Cost:</b> O(n³) expensive matrix inversion.",
                        "<b>Convergence:</b> Quadratic convergence near local minimum."
                    ]
                },
                "summary": "First-order methods scale to big data; second-order methods achieve quadratic convergence.",
                "footer": "Source: mml-book.pdf, Chapter 7"
            }
        ]
    }

    @classmethod
    def get_deck(cls, subject_name: str, chapter_title: str, topic_title: str) -> List[Dict[str, Any]]:
        if topic_title in cls.DECKS:
            return cls.DECKS[topic_title]

        t_clean = topic_title.lower()
        for k, v in cls.DECKS.items():
            if k.lower() in t_clean or t_clean in k.lower():
                return v

        return cls._synthesize_creative_deck(subject_name, chapter_title, topic_title)

    @classmethod
    def _synthesize_creative_deck(cls, subject_name: str, chapter_title: str, topic_title: str) -> List[Dict[str, Any]]:
        return [
            {
                "layout": "hero_split",
                "part": "PART 1 • CONCEPT & INTUITION",
                "title": f"Core Foundations of {topic_title}",
                "subtitle": f"{subject_name} • {chapter_title}",
                "hero": {
                    "badge": "CORE PRINCIPLE",
                    "text": f"<b>{topic_title}</b> forms a fundamental mathematical and algorithmic component of <b>{chapter_title}</b> in the official GATE syllabus. Mastering its governing definitions, boundary conditions, and analytical constraints is essential for solving 1-mark and 2-mark exam questions."
                },
                "left_card": {
                    "header": "Theoretical Scope",
                    "color": cls.C_GREEN,
                    "body": f"• Formal definition and scope under {chapter_title}.<br>• Underlying assumptions: verify whether continuity, discrete domain, or invertibility conditions are required.<br>• Dimension compatibility and domain bounds."
                },
                "right_card": {
                    "header": "GATE Exam Applications",
                    "color": cls.C_RUST,
                    "body": "• Frequently tested in Numerical Answer Type (NAT) calculation problems.<br>• Core foundation for multi-concept questions linking algorithms to mathematical proofs.<br>• Key component in machine learning pipeline reasoning."
                },
                "summary": f"Understand the primary axioms and conditions of {topic_title} before attempting problem solving.",
                "footer": f"Source: Assigned GATE Course Textbooks ({subject_name})"
            },
            {
                "layout": "comparison",
                "part": "PART 2 • METHODOLOGY & COMPARISON",
                "title": f"Key Properties & Analysis: {topic_title}",
                "subtitle": "Comparative analysis and standard analytical methods",
                "left": {
                    "badge": "PRIMARY PROPERTIES",
                    "color": cls.C_BLUE,
                    "points": [
                        "<b>Governing Equation:</b> Standard representation derived in course reference materials.",
                        "<b>Boundary Constraints:</b> Must hold true for analytical solutions to remain valid.",
                        "<b>Asymptotic Limits:</b> Extreme boundary behavior under asymptotic scaling."
                    ]
                },
                "right": {
                    "badge": "COMPUTATIONAL TECHNIQUES",
                    "color": cls.C_PURPLE,
                    "points": [
                        "<b>Extraction:</b> Identify given constants and distribution or matrix parameters.",
                        "<b>Algorithmic Mapping:</b> Relate inputs directly to governing theorems.",
                        "<b>Verification:</b> Confirm results satisfy theoretical bounds (non-negative variance, valid probabilities)."
                    ]
                },
                "summary": "Always verify validity conditions before substituting numerical constants into formulas.",
                "footer": "Source: GATE Examination Preparation Strategy"
            },
            {
                "layout": "traps_dashboard",
                "part": "PART 3 • EXAM TRAPS & NAT REVISION",
                "title": f"High-Yield Pitfalls for {topic_title}",
                "subtitle": "Common mistakes where students lose marks in GATE",
                "traps": [
                    {"icon": "⚠️", "title": "Trap 1: Boundary Assumptions", "color": cls.C_RED, "desc": "Overlooking boundary cases or dividing by zero in intermediate calculation steps."},
                    {"icon": "⚠️", "title": "Trap 2: Formula Pre-conditions", "color": cls.C_ORANGE, "desc": "Applying theorems without first verifying necessary prerequisites (e.g. invertibility or mutual exclusivity)."},
                    {"icon": "💡", "title": "NAT Rounding Shortcut", "color": cls.C_BLUE, "desc": "Keep calculations to 4 decimal places in scratchpad, and round off to 2 decimal places only at the final step."}
                ],
                "summary": "Mastering edge cases turns 1-mark mistakes into confirmed examination scores.",
                "footer": "Source: GATE Examination Revision Guide"
            }
        ]
