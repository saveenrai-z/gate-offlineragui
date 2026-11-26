# =========================================================================
# GATE AI TUTOR - OFFICIAL PRACTICE QUESTION BANK (350+ QUESTIONS)
# 50 Questions per Subject across all 7 Official GATE DA & CS Subjects
# =========================================================================

PRACTICE_QUESTIONS = [
    {
        "id": 1,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "If events A and B are mutually exclusive with P(A) = 0.3 and P(B) = 0.5, what is P(A \u2229 B)?",
        "options": [
            "(A) 0.15",
            "(B) 0",
            "(C) 0.8",
            "(D) 0.2"
        ],
        "correct_answer": "B",
        "explanation": "By definition of mutually exclusive events, they cannot occur simultaneously, meaning A \u2229 B = \u2205. Therefore, P(A \u2229 B) = 0."
    },
    {
        "id": 2,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "If events A and B are independent with P(A) = 0.4 and P(B) = 0.5, what is P(A \u222a B)?",
        "options": [
            "(A) 0.9",
            "(B) 0.7",
            "(C) 0.2",
            "(D) 0.6"
        ],
        "correct_answer": "B",
        "explanation": "P(A \u2229 B) = P(A) * P(B) = 0.2. P(A \u222a B) = P(A) + P(B) - P(A \u2229 B) = 0.4 + 0.5 - 0.2 = 0.7."
    },
    {
        "id": 3,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Under Kolmogorov's third axiom, if A_1, A_2, ... is a countable sequence of pairwise disjoint events, then P(\u222a A_i) equals:",
        "options": [
            "(A) \u220f P(A_i)",
            "(B) \u2211 P(A_i)",
            "(C) max P(A_i)",
            "(D) 1 - \u220f (1 - P(A_i))"
        ],
        "correct_answer": "B",
        "explanation": "Kolmogorov's third axiom (Countable Additivity) states that P(\u222a A_i) = \u2211 P(A_i) for disjoint events."
    },
    {
        "id": 4,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "A fair coin is tossed 3 times. What is the probability of obtaining at least two heads?",
        "options": [
            "(A) 1/8",
            "(B) 3/8",
            "(C) 1/2",
            "(D) 5/8"
        ],
        "correct_answer": "C",
        "explanation": "Outcomes with \u2265 2 heads: HHH, HHT, HTH, THH (4 outcomes out of 8). Probability = 4/8 = 1/2."
    },
    {
        "id": 5,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "A box contains 4 red and 6 black balls. Two balls are drawn successively without replacement. Probability that both are red is:",
        "options": [
            "(A) 4/25",
            "(B) 2/15",
            "(C) 6/15",
            "(D) 1/5"
        ],
        "correct_answer": "B",
        "explanation": "P(R1) = 4/10. P(R2|R1) = 3/9. P(R1 \u2229 R2) = (4/10) * (3/9) = 12/90 = 2/15."
    },
    {
        "id": 6,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "If P(A) = 0.6, P(B) = 0.4, and P(A|B) = 0.7, what is P(B|A)?",
        "options": [
            "(A) 0.467",
            "(B) 0.28",
            "(C) 0.42",
            "(D) 0.70"
        ],
        "correct_answer": "A",
        "explanation": "P(A \u2229 B) = P(A|B) * P(B) = 0.7 * 0.4 = 0.28. P(B|A) = P(A \u2229 B) / P(A) = 0.28 / 0.6 = 7/15 \u2248 0.467."
    },
    {
        "id": 7,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "A disease has 1% prevalence. A test has 95% sensitivity and 90% specificity. If someone tests positive, probability they have the disease is:",
        "options": [
            "(A) 0.95",
            "(B) 0.50",
            "(C) 0.0876",
            "(D) 0.01"
        ],
        "correct_answer": "C",
        "explanation": "P(+) = (0.95 * 0.01) + (0.10 * 0.99) = 0.1085. P(D|+) = 0.0095 / 0.1085 \u2248 0.0876 (approx 8.8%)."
    },
    {
        "id": 8,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Let X have PMF P(X = k) = c * (1/3)^k for k = 1, 2, 3, ... The value of c is:",
        "options": [
            "(A) 1/3",
            "(B) 2/3",
            "(C) 2",
            "(D) 3/2"
        ],
        "correct_answer": "C",
        "explanation": "\u2211_{k=1}^\u221e c (1/3)^k = c * [(1/3)/(1 - 1/3)] = c/2 = 1 => c = 2."
    },
    {
        "id": 9,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "For random variable X with E[X] = 5 and Var(X) = 4, what is E[X^2]?",
        "options": [
            "(A) 21",
            "(B) 25",
            "(C) 29",
            "(D) 9"
        ],
        "correct_answer": "C",
        "explanation": "E[X^2] = Var(X) + (E[X])^2 = 4 + 25 = 29."
    },
    {
        "id": 10,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "If Var(X) = 9, what is Var(-3X + 7)?",
        "options": [
            "(A) -27",
            "(B) 34",
            "(C) 81",
            "(D) 88"
        ],
        "correct_answer": "C",
        "explanation": "Var(aX + b) = a^2 Var(X) = (-3)^2 * 9 = 81."
    },
    {
        "id": 11,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "X ~ Binomial(n = 10, p = 0.3). What is Var(X)?",
        "options": [
            "(A) 3.0",
            "(B) 2.1",
            "(C) 0.7",
            "(D) 1.5"
        ],
        "correct_answer": "B",
        "explanation": "Var(X) = np(1-p) = 10 * 0.3 * 0.7 = 2.1."
    },
    {
        "id": 12,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "X ~ Poisson(\u03bb). If P(X = 1) = P(X = 2), what is \u03bb?",
        "options": [
            "(A) 1",
            "(B) 2",
            "(C) 0.5",
            "(D) 4"
        ],
        "correct_answer": "B",
        "explanation": "e^{-\u03bb} \u03bb = e^{-\u03bb} \u03bb^2 / 2 => 1 = \u03bb/2 => \u03bb = 2."
    },
    {
        "id": 13,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "X ~ Poisson with mean 3. What is Var(2X - 5)?",
        "options": [
            "(A) 6",
            "(B) 12",
            "(C) 1",
            "(D) 7"
        ],
        "correct_answer": "B",
        "explanation": "Var(X) = \u03bb = 3. Var(2X - 5) = 4 * 3 = 12."
    },
    {
        "id": 14,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "X ~ Geometric(p), P(X = k) = (1-p)^{k-1} p. E[X] equals:",
        "options": [
            "(A) p",
            "(B) 1/p",
            "(C) (1-p)/p",
            "(D) 1/p^2"
        ],
        "correct_answer": "B",
        "explanation": "Expected trials until first success in geometric distribution is 1/p."
    },
    {
        "id": 15,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "The memoryless property P(X > s + t | X > s) = P(X > t) holds for which discrete distribution?",
        "options": [
            "(A) Binomial",
            "(B) Poisson",
            "(C) Geometric",
            "(D) Hypergeometric"
        ],
        "correct_answer": "C",
        "explanation": "Geometric distribution is the unique memoryless discrete distribution."
    },
    {
        "id": 16,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "By Chebyshev's inequality, P(|X - \u03bc| \u2265 k\u03c3) is bounded above by:",
        "options": [
            "(A) 1/k",
            "(B) 1/k^2",
            "(C) 1 - 1/k^2",
            "(D) k^2"
        ],
        "correct_answer": "B",
        "explanation": "Chebyshev's inequality guarantees P(|X - \u03bc| \u2265 k\u03c3) \u2264 1/k^2."
    },
    {
        "id": 17,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "X has mean 20 and std dev 2. By Chebyshev's inequality, P(16 < X < 24) is at least:",
        "options": [
            "(A) 0.50",
            "(B) 0.75",
            "(C) 0.889",
            "(D) 0.95"
        ],
        "correct_answer": "B",
        "explanation": "|X - 20| < 4 = 2\u03c3 => k = 2. Bound \u2265 1 - 1/k^2 = 1 - 1/4 = 0.75."
    },
    {
        "id": 18,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "If X and Y are independent random variables, Cov(X, Y) is:",
        "options": [
            "(A) 1",
            "(B) E[X]E[Y]",
            "(C) 0",
            "(D) Var(X)Var(Y)"
        ],
        "correct_answer": "C",
        "explanation": "Independence implies E[XY] = E[X]E[Y], hence Cov(X, Y) = 0."
    },
    {
        "id": 19,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Var(X) = 4, Var(Y) = 9, Cov(X, Y) = 2. What is Var(X - Y)?",
        "options": [
            "(A) 9",
            "(B) 17",
            "(C) 13",
            "(D) 5"
        ],
        "correct_answer": "A",
        "explanation": "Var(X - Y) = Var(X) + Var(Y) - 2 Cov(X, Y) = 4 + 9 - 4 = 9."
    },
    {
        "id": 20,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "If P(A \u2229 B) = 0.2 and P(A \u2229 B^c) = 0.3, what is P(A)?",
        "options": [
            "(A) 0.1",
            "(B) 0.5",
            "(C) 0.6",
            "(D) 0.06"
        ],
        "correct_answer": "B",
        "explanation": "P(A) = P(A \u2229 B) + P(A \u2229 B^c) = 0.2 + 0.3 = 0.5."
    },
    {
        "id": 21,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "X takes values {-1, 0, 1} with probabilities {0.25, 0.5, 0.25}. E[X] and Var(X) are:",
        "options": [
            "(A) 0 and 0.5",
            "(B) 0 and 0.25",
            "(C) 0.5 and 0.5",
            "(D) 0 and 1.0"
        ],
        "correct_answer": "A",
        "explanation": "E[X] = 0. E[X^2] = 0.25 + 0.25 = 0.5. Var(X) = 0.5 - 0 = 0.5."
    },
    {
        "id": 22,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Independent events A and B have P(A) = 0.3, P(B) = 0.4. What is P(A^c \u2229 B^c)?",
        "options": [
            "(A) 0.12",
            "(B) 0.58",
            "(C) 0.42",
            "(D) 0.70"
        ],
        "correct_answer": "C",
        "explanation": "P(A^c \u2229 B^c) = P(A^c) P(B^c) = 0.7 * 0.6 = 0.42."
    },
    {
        "id": 23,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Which of the following is NOT a mandatory condition for a valid CDF F(x)?",
        "options": [
            "(A) Non-decreasing",
            "(B) lim_{x->-\u221e} F(x) = 0",
            "(C) Strictly continuous everywhere",
            "(D) Right-continuous"
        ],
        "correct_answer": "C",
        "explanation": "CDFs for discrete variables have step discontinuities, so continuity everywhere is not mandatory."
    },
    {
        "id": 24,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Two fair dice are rolled. Probability that the sum is 7 equals:",
        "options": [
            "(A) 1/12",
            "(B) 5/36",
            "(C) 1/6",
            "(D) 7/36"
        ],
        "correct_answer": "C",
        "explanation": "Favorable outcomes = 6. Total = 36. 6/36 = 1/6."
    },
    {
        "id": 25,
        "subject": "Probability and Statistics",
        "chapter": "Probability Axioms & Random Variables",
        "question": "Mutual independence of three events requires pairwise independence plus:",
        "options": [
            "(A) P(A \u222a B \u222a C) = 1",
            "(B) P(A \u2229 B \u2229 C) = P(A)P(B)P(C)",
            "(C) P(A|B) = P(B|C)",
            "(D) P(A \u2229 B) = 0"
        ],
        "correct_answer": "B",
        "explanation": "Joint product condition P(A \u2229 B \u2229 C) = P(A)P(B)P(C) is required."
    },
    {
        "id": 26,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Continuous variable X has PDF f(x) = k*x for 0 \u2264 x \u2264 2. Value of k is:",
        "options": [
            "(A) 1/4",
            "(B) 1/2",
            "(C) 1",
            "(D) 2"
        ],
        "correct_answer": "B",
        "explanation": "\u222b_0^2 k*x dx = 2k = 1 => k = 1/2."
    },
    {
        "id": 27,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "For uniform distribution X ~ U(a, b), the variance is:",
        "options": [
            "(A) (b-a)/2",
            "(B) (b-a)^2/12",
            "(C) (b-a)^2/4",
            "(D) (b+a)^2/12"
        ],
        "correct_answer": "B",
        "explanation": "Var(X) for U(a, b) is (b - a)^2 / 12."
    },
    {
        "id": 28,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If X ~ N(10, 4), what is the standardized value Z for X = 14?",
        "options": [
            "(A) 1",
            "(B) 2",
            "(C) 4",
            "(D) 0.5"
        ],
        "correct_answer": "B",
        "explanation": "\u03c3 = 2. Z = (14 - 10)/2 = 2."
    },
    {
        "id": 29,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "For standard normal Z ~ N(0, 1), P(Z < 0) equals:",
        "options": [
            "(A) 0",
            "(B) 0.5",
            "(C) 1.0",
            "(D) 0.68"
        ],
        "correct_answer": "B",
        "explanation": "Symmetric about 0, so exactly half the probability lies below 0."
    },
    {
        "id": 30,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "By Central Limit Theorem, the sample mean X\u0304 of i.i.d. samples approaches:",
        "options": [
            "(A) Uniform",
            "(B) N(\u03bc, \u03c3^2/n)",
            "(C) Poisson",
            "(D) N(n\u03bc, n\u03c3^2)"
        ],
        "correct_answer": "B",
        "explanation": "Distribution of X\u0304 approaches Normal with mean \u03bc and variance \u03c3^2 / n."
    },
    {
        "id": 31,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "X ~ Exponential with rate \u03bb = 0.5. The mean E[X] is:",
        "options": [
            "(A) 0.5",
            "(B) 1.0",
            "(C) 2.0",
            "(D) 4.0"
        ],
        "correct_answer": "C",
        "explanation": "E[X] = 1/\u03bb = 1/0.5 = 2.0."
    },
    {
        "id": 32,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Continuous distribution with memoryless property P(X > s+t | X > s) = P(X > t) is:",
        "options": [
            "(A) Normal",
            "(B) Exponential",
            "(C) Gamma",
            "(D) Beta"
        ],
        "correct_answer": "B",
        "explanation": "Exponential distribution is the unique continuous memoryless distribution."
    },
    {
        "id": 33,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If correlation \u03c1(X, Y) = 0.8, what is \u03c1(2X + 3, -4Y + 1)?",
        "options": [
            "(A) 0.8",
            "(B) -0.8",
            "(C) 1.6",
            "(D) -0.4"
        ],
        "correct_answer": "B",
        "explanation": "Sign of (2 * -4) is negative, so correlation flips sign: -0.8."
    },
    {
        "id": 34,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Pearson correlation coefficient \u03c1(X, Y) is bounded within:",
        "options": [
            "(A) [0, 1]",
            "(B) (-\u221e, \u221e)",
            "(C) [-1, 1]",
            "(D) [-0.5, 0.5]"
        ],
        "correct_answer": "C",
        "explanation": "By Cauchy-Schwarz inequality, -1 \u2264 \u03c1 \u2264 1."
    },
    {
        "id": 35,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If Y = 5 - 2X, what is the correlation coefficient between X and Y?",
        "options": [
            "(A) -2",
            "(B) 1",
            "(C) -1",
            "(D) 0"
        ],
        "correct_answer": "C",
        "explanation": "Perfect negative linear relationship yields \u03c1 = -1."
    },
    {
        "id": 36,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "In MLE for i.i.d. Bernoulli(p) samples, the estimator p\u0302 is:",
        "options": [
            "(A) Sample mean (1/n) \u2211 X_i",
            "(B) max(X_i)",
            "(C) n / \u2211 X_i",
            "(D) \u2211 X_i"
        ],
        "correct_answer": "A",
        "explanation": "Solving d/dp ln L(p) = 0 gives sample mean p\u0302 = (1/n) \u2211 x_i."
    },
    {
        "id": 37,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "An estimator \u03b8\u0302 is unbiased if:",
        "options": [
            "(A) Var(\u03b8\u0302) = 0",
            "(B) E[\u03b8\u0302] = \u03b8",
            "(C) lim \u03b8\u0302 = \u03b8",
            "(D) \u03b8\u0302 = \u03b8"
        ],
        "correct_answer": "B",
        "explanation": "Unbiasedness requires expected value to equal true parameter: E[\u03b8\u0302] = \u03b8."
    },
    {
        "id": 38,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Bessel's correction uses (n - 1) in sample variance s^2 to:",
        "options": [
            "(A) Reduce computation",
            "(B) Make s^2 an unbiased estimator of \u03c3^2",
            "(C) Maximize likelihood",
            "(D) Ensure positivity"
        ],
        "correct_answer": "B",
        "explanation": "Dividing by (n - 1) ensures E[s^2] = \u03c3^2."
    },
    {
        "id": 39,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Type I error occurs when:",
        "options": [
            "(A) Accept false H_0",
            "(B) Reject true H_0",
            "(C) Test statistic is 0",
            "(D) Small sample"
        ],
        "correct_answer": "B",
        "explanation": "Type I error is false rejection of a true null hypothesis (probability \u03b1)."
    },
    {
        "id": 40,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Type II error occurs when:",
        "options": [
            "(A) Reject true H_0",
            "(B) Fail to reject false H_0",
            "(C) Both true",
            "(D) p-value is 0"
        ],
        "correct_answer": "B",
        "explanation": "Type II error is false acceptance of a false null hypothesis (probability \u03b2)."
    },
    {
        "id": 41,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Statistical power of a hypothesis test equals:",
        "options": [
            "(A) 1 - \u03b1",
            "(B) \u03b1 + \u03b2",
            "(C) 1 - \u03b2",
            "(D) \u03b2 / \u03b1"
        ],
        "correct_answer": "C",
        "explanation": "Power is the probability of correctly rejecting a false null: 1 - \u03b2."
    },
    {
        "id": 42,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If p-value = 0.02 and significance level \u03b1 = 0.05, the conclusion is:",
        "options": [
            "(A) Accept H_0",
            "(B) Reject H_0 because p-value < \u03b1",
            "(C) Increase sample",
            "(D) Inconclusive"
        ],
        "correct_answer": "B",
        "explanation": "p-value < \u03b1 indicates statistical significance; reject H_0."
    },
    {
        "id": 43,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Joint PDF f(x, y) = 4xy on [0,1]x[0,1]. Marginal PDF f_X(x) is:",
        "options": [
            "(A) 2x",
            "(B) 4x",
            "(C) x^2",
            "(D) 2x^2"
        ],
        "correct_answer": "A",
        "explanation": "\u222b_0^1 4xy dy = 4x [y^2/2]_0^1 = 2x."
    },
    {
        "id": 44,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If joint PDF factors as f(x, y) = g(x) * h(y) on rectangular domain, X and Y are:",
        "options": [
            "(A) Mutually exclusive",
            "(B) Dependent",
            "(C) Independent",
            "(D) Identical"
        ],
        "correct_answer": "C",
        "explanation": "Factorization of joint density is necessary and sufficient for independence."
    },
    {
        "id": 45,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Independent standard normal X, Y ~ N(0, 1). Distribution of X + Y is:",
        "options": [
            "(A) N(0, 1)",
            "(B) N(0, 2)",
            "(C) U(0, 2)",
            "(D) Chi-squared(2)"
        ],
        "correct_answer": "B",
        "explanation": "Sum is normal with mean 0+0=0 and variance 1+1=2."
    },
    {
        "id": 46,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If Z ~ N(0, 1), the distribution of Z^2 is:",
        "options": [
            "(A) Normal N(0, 1)",
            "(B) Chi-Square with 1 d.o.f.",
            "(C) Exponential(1)",
            "(D) Student t(1)"
        ],
        "correct_answer": "B",
        "explanation": "Square of standard normal is Chi-Square with 1 degree of freedom."
    },
    {
        "id": 47,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "In 95% two-sided confidence interval for mean with known variance, critical Z is:",
        "options": [
            "(A) 1.645",
            "(B) 1.96",
            "(C) 2.576",
            "(D) 3.00"
        ],
        "correct_answer": "B",
        "explanation": "Z_{0.025} for two-tailed 95% interval is approximately 1.96."
    },
    {
        "id": 48,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "For i.i.d. samples from Exponential(\u03bb), the MLE estimator for \u03bb is:",
        "options": [
            "(A) X\u0304",
            "(B) 1 / X\u0304",
            "(C) n * X\u0304",
            "(D) X\u0304^2"
        ],
        "correct_answer": "B",
        "explanation": "Maximizing likelihood yields \u03bb\u0302 = 1 / X\u0304."
    },
    {
        "id": 49,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "If X has continuous CDF F(x), what is the distribution of U = F(X)?",
        "options": [
            "(A) Normal",
            "(B) Uniform U(0, 1)",
            "(C) Exponential",
            "(D) Beta"
        ],
        "correct_answer": "B",
        "explanation": "Probability Integral Transform proves F(X) ~ Uniform(0, 1)."
    },
    {
        "id": 50,
        "subject": "Probability and Statistics",
        "chapter": "Distributions & Statistics",
        "question": "Can two events with P(A) > 0 and P(B) > 0 be both mutually exclusive and independent?",
        "options": [
            "(A) Yes, always",
            "(B) No, never",
            "(C) Only if P(A)+P(B)=1",
            "(D) Only if P(A)=P(B)"
        ],
        "correct_answer": "B",
        "explanation": "Mutually exclusive implies P(A \u2229 B) = 0, while independence implies P(A \u2229 B) > 0. Contradiction."
    },
    {
        "id": 51,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "For an m x n matrix A, the Rank-Nullity Theorem states that Rank(A) + Nullity(A) equals:",
        "options": [
            "(A) m",
            "(B) n",
            "(C) m + n",
            "(D) min(m, n)"
        ],
        "correct_answer": "B",
        "explanation": "The Rank-Nullity theorem states dim(Col A) + dim(Null A) = n (number of columns / dimension of domain)."
    },
    {
        "id": 52,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is an n x n invertible matrix, which of the following is FALSE?",
        "options": [
            "(A) det(A) \u2260 0",
            "(B) Rank(A) = n",
            "(C) Ax = 0 has a non-trivial solution",
            "(D) Columns of A are linearly independent"
        ],
        "correct_answer": "C",
        "explanation": "For an invertible matrix, Ax = 0 has ONLY the trivial solution x = 0."
    },
    {
        "id": 53,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "What is the determinant of a 3x3 matrix whose eigenvalues are 2, -3, and 5?",
        "options": [
            "(A) 4",
            "(B) -30",
            "(C) 30",
            "(D) 0"
        ],
        "correct_answer": "B",
        "explanation": "Determinant of a matrix equals the product of its eigenvalues: 2 * (-3) * 5 = -30."
    },
    {
        "id": 54,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is a 4x4 matrix and det(A) = 3, what is det(2A)?",
        "options": [
            "(A) 6",
            "(B) 12",
            "(C) 24",
            "(D) 48"
        ],
        "correct_answer": "D",
        "explanation": "For an n x n matrix, det(cA) = c^n det(A). Here n = 4, so det(2A) = 2^4 * 3 = 16 * 3 = 48."
    },
    {
        "id": 55,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "A system of linear equations Ax = b has a unique solution if and only if:",
        "options": [
            "(A) Rank(A) = Rank([A|b]) < n",
            "(B) Rank(A) = Rank([A|b]) = n",
            "(C) Rank(A) < Rank([A|b])",
            "(D) det(A) = 0"
        ],
        "correct_answer": "B",
        "explanation": "By Rouch\u00e9-Capelli theorem, unique solution requires Rank(A) = Rank([A|b]) = n (number of unknowns)."
    },
    {
        "id": 56,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "A system of linear equations Ax = b has NO solution when:",
        "options": [
            "(A) Rank(A) = Rank([A|b])",
            "(B) Rank(A) < Rank([A|b])",
            "(C) Rank(A) = n",
            "(D) b = 0"
        ],
        "correct_answer": "B",
        "explanation": "If the augmented matrix has greater rank than the coefficient matrix, the system is inconsistent (no solution)."
    },
    {
        "id": 57,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "Which of the following subsets of R^3 is a valid vector subspace?",
        "options": [
            "(A) {(x, y, z) : x + y + z = 1}",
            "(B) {(x, y, z) : x = 2y and z = 0}",
            "(C) {(x, y, z) : xy = 0}",
            "(D) {(x, y, z) : x \u2265 0}"
        ],
        "correct_answer": "B",
        "explanation": "Option B contains (0,0,0) and is closed under addition and scalar multiplication (plane/line through origin). Option A doesn't contain origin; C fails addition; D fails negative scalars."
    },
    {
        "id": 58,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If vectors v_1, v_2, v_3 in R^3 are linearly dependent, what is the maximum possible rank of [v_1, v_2, v_3]?",
        "options": [
            "(A) 0",
            "(B) 1",
            "(C) 2",
            "(D) 3"
        ],
        "correct_answer": "C",
        "explanation": "If 3 vectors in R^3 are dependent, their span has dimension at most 2, so rank cannot be 3."
    },
    {
        "id": 59,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is a 5x3 matrix and B is a 3x4 matrix, what is the maximum possible rank of AB?",
        "options": [
            "(A) 5",
            "(B) 4",
            "(C) 3",
            "(D) 12"
        ],
        "correct_answer": "C",
        "explanation": "Rank(AB) \u2264 min(Rank(A), Rank(B)) \u2264 min(3, 3) = 3."
    },
    {
        "id": 60,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "Let U and W be subspaces of R^n. Under what condition is U \u222a W guaranteed to be a subspace?",
        "options": [
            "(A) Always",
            "(B) If and only if U \u2286 W or W \u2286 U",
            "(C) If U \u2229 W = {0}",
            "(D) Never"
        ],
        "correct_answer": "B",
        "explanation": "The union of two subspaces is a subspace if and only if one is a subset of the other."
    },
    {
        "id": 61,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "For subspaces U and W, the dimension formula dim(U + W) is given by:",
        "options": [
            "(A) dim(U) + dim(W)",
            "(B) dim(U) + dim(W) - dim(U \u2229 W)",
            "(C) dim(U) * dim(W)",
            "(D) max(dim U, dim W)"
        ],
        "correct_answer": "B",
        "explanation": "dim(U + W) = dim(U) + dim(W) - dim(U \u2229 W)."
    },
    {
        "id": 62,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is a skew-symmetric matrix (A^T = -A) of odd order n, its determinant MUST be:",
        "options": [
            "(A) 1",
            "(B) -1",
            "(C) 0",
            "(D) Any real number"
        ],
        "correct_answer": "C",
        "explanation": "det(A) = det(A^T) = det(-A) = (-1)^n det(A). If n is odd, det(A) = -det(A) => 2 det(A) = 0 => det(A) = 0."
    },
    {
        "id": 63,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is an orthogonal matrix (A^T A = I), what are the possible values of det(A)?",
        "options": [
            "(A) Only 1",
            "(B) 0 or 1",
            "(C) +1 or -1",
            "(D) Any positive number"
        ],
        "correct_answer": "C",
        "explanation": "det(A^T A) = det(I) => (det A)^2 = 1 => det(A) = \u00b11."
    },
    {
        "id": 64,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "What is the inverse of an orthogonal matrix Q?",
        "options": [
            "(A) Q",
            "(B) Q^T",
            "(C) -Q",
            "(D) det(Q) * Q"
        ],
        "correct_answer": "B",
        "explanation": "By definition of orthogonal matrix, Q^T Q = Q Q^T = I, so Q^{-1} = Q^T."
    },
    {
        "id": 65,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "Elementary row operations on matrix A preserve:",
        "options": [
            "(A) Column space",
            "(B) Row space and Rank",
            "(C) Eigenvalues",
            "(D) Trace"
        ],
        "correct_answer": "B",
        "explanation": "Row operations preserve linear relations between rows, keeping row space and rank invariant."
    },
    {
        "id": 66,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is an n x n matrix with Rank(A) = r < n, how many linearly independent solutions does Ax = 0 have?",
        "options": [
            "(A) r",
            "(B) n - r",
            "(C) n",
            "(D) 0"
        ],
        "correct_answer": "B",
        "explanation": "By Rank-Nullity theorem, Nullity(A) = n - r, which is the dimension of the null space."
    },
    {
        "id": 67,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A and B are square matrices of same size, which statement is generally FALSE?",
        "options": [
            "(A) det(AB) = det(A) det(B)",
            "(B) (AB)^T = B^T A^T",
            "(C) AB = BA",
            "(D) Trace(AB) = Trace(BA)"
        ],
        "correct_answer": "C",
        "explanation": "Matrix multiplication is generally non-commutative (AB \u2260 BA in general)."
    },
    {
        "id": 68,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is idempotent (A^2 = A), what are its possible eigenvalues?",
        "options": [
            "(A) 1 and -1",
            "(B) 0 and 1",
            "(C) Only 0",
            "(D) Any integer"
        ],
        "correct_answer": "B",
        "explanation": "A v = \u03bb v => A^2 v = \u03bb^2 v = \u03bb v => \u03bb^2 - \u03bb = 0 => \u03bb(\u03bb - 1) = 0 => \u03bb \u2208 {0, 1}."
    },
    {
        "id": 69,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is nilpotent (A^k = 0 for some k), all eigenvalues of A are:",
        "options": [
            "(A) 1",
            "(B) -1",
            "(C) 0",
            "(D) Purely imaginary"
        ],
        "correct_answer": "C",
        "explanation": "A^k v = \u03bb^k v = 0 => \u03bb^k = 0 => \u03bb = 0."
    },
    {
        "id": 70,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "The trace of an n x n matrix equals:",
        "options": [
            "(A) Product of eigenvalues",
            "(B) Sum of eigenvalues",
            "(C) Determinant of A",
            "(D) Rank of A"
        ],
        "correct_answer": "B",
        "explanation": "Trace(A) = \u2211 a_{ii} = \u2211 \u03bb_i (sum of eigenvalues)."
    },
    {
        "id": 71,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If matrix A has eigenvalues 1, 2, 3, what are the eigenvalues of A^2?",
        "options": [
            "(A) 1, 2, 3",
            "(B) 1, 4, 9",
            "(C) 2, 4, 6",
            "(D) 1/1, 1/2, 1/3"
        ],
        "correct_answer": "B",
        "explanation": "If \u03bb is an eigenvalue of A, then \u03bb^k is an eigenvalue of A^k. 1^2 = 1, 2^2 = 4, 3^2 = 9."
    },
    {
        "id": 72,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "If A is nonsingular with eigenvalues \u03bb_i, eigenvalues of A^{-1} are:",
        "options": [
            "(A) -\u03bb_i",
            "(B) 1 / \u03bb_i",
            "(C) \u03bb_i^2",
            "(D) 1 - \u03bb_i"
        ],
        "correct_answer": "B",
        "explanation": "A v = \u03bb v => v = \u03bb A^{-1} v => A^{-1} v = (1/\u03bb) v."
    },
    {
        "id": 73,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "The coordinate vector of v = [3, 5]^T with respect to standard basis {e_1, e_2} is:",
        "options": [
            "(A) [5, 3]^T",
            "(B) [3, 5]^T",
            "(C) [8, 2]^T",
            "(D) [1, 1]^T"
        ],
        "correct_answer": "B",
        "explanation": "v = 3 [1, 0]^T + 5 [0, 1]^T = [3, 5]^T."
    },
    {
        "id": 74,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "What is the dimension of the vector space of all 3x3 symmetric matrices?",
        "options": [
            "(A) 9",
            "(B) 6",
            "(C) 3",
            "(D) 5"
        ],
        "correct_answer": "B",
        "explanation": "For an n x n symmetric matrix, independent entries = n(n+1)/2. For n = 3: 3*4/2 = 6."
    },
    {
        "id": 75,
        "subject": "Linear Algebra",
        "chapter": "Matrices and Systems of Equations",
        "question": "What is the dimension of the vector space of all 3x3 skew-symmetric matrices?",
        "options": [
            "(A) 9",
            "(B) 6",
            "(C) 3",
            "(D) 0"
        ],
        "correct_answer": "C",
        "explanation": "Diagonal entries must be 0; independent entries above diagonal = n(n-1)/2 = 3*2/2 = 3."
    },
    {
        "id": 76,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "By the Cayley-Hamilton theorem, every square matrix satisfies its own:",
        "options": [
            "(A) Linear system",
            "(B) Characteristic equation",
            "(C) Transpose",
            "(D) SVD decomposition"
        ],
        "correct_answer": "B",
        "explanation": "Cayley-Hamilton states p(A) = 0 where p(\u03bb) = det(A - \u03bbI) is the characteristic polynomial."
    },
    {
        "id": 77,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "An n x n real symmetric matrix ALWAYS has:",
        "options": [
            "(A) Complex eigenvalues",
            "(B) Real eigenvalues and orthogonal eigenvectors",
            "(C) Zero determinant",
            "(D) Negative trace"
        ],
        "correct_answer": "B",
        "explanation": "The Spectral Theorem guarantees real eigenvalues and orthonormal eigenvectors for real symmetric matrices."
    },
    {
        "id": 78,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "A real symmetric matrix A is Positive Definite (A \u227b 0) if and only if:",
        "options": [
            "(A) All eigenvalues are strictly positive",
            "(B) All eigenvalues are non-negative",
            "(C) det(A) > 0",
            "(D) Trace(A) > 0"
        ],
        "correct_answer": "A",
        "explanation": "Positive definiteness requires all eigenvalues \u03bb_i > 0 (or all leading principal minors > 0)."
    },
    {
        "id": 79,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If A is positive semi-definite (A \u2ab0 0), which condition is TRUE?",
        "options": [
            "(A) All eigenvalues are \u2265 0",
            "(B) det(A) is strictly positive",
            "(C) A is invertible",
            "(D) All eigenvalues are < 0"
        ],
        "correct_answer": "A",
        "explanation": "Positive semi-definite requires x^T A x \u2265 0 for all x, which is equivalent to all \u03bb_i \u2265 0."
    },
    {
        "id": 80,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "An n x n matrix A is diagonalizable if and only if:",
        "options": [
            "(A) det(A) \u2260 0",
            "(B) A has n linearly independent eigenvectors",
            "(C) A has distinct diagonal elements",
            "(D) A is symmetric"
        ],
        "correct_answer": "B",
        "explanation": "Diagonalizability requires algebraic multiplicity = geometric multiplicity for all eigenvalues (n independent eigenvectors)."
    },
    {
        "id": 81,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If an n x n matrix has n DISTINCT eigenvalues, then the matrix is:",
        "options": [
            "(A) Always diagonalizable",
            "(B) Never diagonalizable",
            "(C) Always singular",
            "(D) Orthogonal"
        ],
        "correct_answer": "A",
        "explanation": "Distinct eigenvalues strictly imply linearly independent eigenvectors, guaranteeing diagonalizability."
    },
    {
        "id": 82,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "The algebraic multiplicity of an eigenvalue \u03bb is the multiplicity of \u03bb as a root of:",
        "options": [
            "(A) Minimal polynomial",
            "(B) Characteristic polynomial",
            "(C) Eigenspace dimension",
            "(D) Determinant"
        ],
        "correct_answer": "B",
        "explanation": "Algebraic multiplicity is the power of (x - \u03bb) in det(A - xI). Geometric multiplicity is dim(Null(A - \u03bbI))."
    },
    {
        "id": 83,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "In Gram-Schmidt orthogonalization on vectors {v_1, v_2}, the orthogonal vector u_2 is:",
        "options": [
            "(A) v_2 - proj_{u_1}(v_2)",
            "(B) v_2 + proj_{u_1}(v_2)",
            "(C) u_1 - v_2",
            "(D) v_1 + v_2"
        ],
        "correct_answer": "A",
        "explanation": "u_2 = v_2 - ( (v_2 \u00b7 u_1) / (u_1 \u00b7 u_1) ) u_1."
    },
    {
        "id": 84,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "In Singular Value Decomposition (SVD) A = U \u03a3 V^T for an m x n matrix, the singular values \u03c3_i are:",
        "options": [
            "(A) Eigenvalues of A",
            "(B) Square roots of non-negative eigenvalues of A^T A",
            "(C) Determinant of A",
            "(D) Diagonal entries of A"
        ],
        "correct_answer": "B",
        "explanation": "Singular values are \u03c3_i = \u221a(\u03bb_i(A^T A))."
    },
    {
        "id": 85,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If A has singular values 5, 3, 0, what is the rank of A?",
        "options": [
            "(A) 3",
            "(B) 2",
            "(C) 1",
            "(D) 8"
        ],
        "correct_answer": "B",
        "explanation": "The rank of a matrix equals the number of non-zero singular values in its SVD: 2."
    },
    {
        "id": 86,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "In SVD A = U \u03a3 V^T, matrices U and V are:",
        "options": [
            "(A) Diagonal",
            "(B) Orthogonal (unitary)",
            "(C) Symmetric",
            "(D) Triangular"
        ],
        "correct_answer": "B",
        "explanation": "U is an m x m orthogonal matrix and V is an n x n orthogonal matrix."
    },
    {
        "id": 87,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "The condition number \u03ba(A) of an invertible matrix in 2-norm is given by:",
        "options": [
            "(A) \u03c3_max / \u03c3_min",
            "(B) \u03c3_max - \u03c3_min",
            "(C) det(A)",
            "(D) Trace(A)"
        ],
        "correct_answer": "A",
        "explanation": "In 2-norm, \u03ba(A) = ||A||_2 ||A^{-1}||_2 = \u03c3_1 / \u03c3_n (ratio of largest to smallest singular value)."
    },
    {
        "id": 88,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "The projection matrix P onto a subspace with orthonormal basis columns Q is:",
        "options": [
            "(A) Q Q^T",
            "(B) Q^T Q",
            "(C) Q^{-1}",
            "(D) (Q^T Q)^{-1}"
        ],
        "correct_answer": "A",
        "explanation": "When columns of Q are orthonormal, P = Q (Q^T Q)^{-1} Q^T = Q I Q^T = Q Q^T."
    },
    {
        "id": 89,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "A projection matrix P satisfies which two fundamental properties?",
        "options": [
            "(A) P^2 = P and P^T = P",
            "(B) P^2 = I and P^T = -P",
            "(C) det(P) = 1 and Trace(P) = 0",
            "(D) P = P^{-1}"
        ],
        "correct_answer": "A",
        "explanation": "Orthogonal projection matrices are idempotent (P^2 = P) and symmetric (P^T = P)."
    },
    {
        "id": 90,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "What are the eigenvalues of any projection matrix P?",
        "options": [
            "(A) Only 1",
            "(B) Only 0 and 1",
            "(C) Real numbers > 1",
            "(D) \u00b11"
        ],
        "correct_answer": "B",
        "explanation": "Since P^2 = P, \u03bb^2 = \u03bb => \u03bb \u2208 {0, 1}."
    },
    {
        "id": 91,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "The Moore-Penrose pseudo-inverse A^+ of full column rank matrix A is:",
        "options": [
            "(A) A^T",
            "(B) (A^T A)^{-1} A^T",
            "(C) A^T (A A^T)^{-1}",
            "(D) A^{-1}"
        ],
        "correct_answer": "B",
        "explanation": "For full column rank, A^+ = (A^T A)^{-1} A^T (left inverse)."
    },
    {
        "id": 92,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "The Cauchy-Schwarz inequality states that for vectors u and v:",
        "options": [
            "(A) |u \u00b7 v| \u2264 ||u|| ||v||",
            "(B) |u \u00b7 v| \u2265 ||u|| ||v||",
            "(C) ||u + v|| = ||u|| + ||v||",
            "(D) u \u00b7 v = 0"
        ],
        "correct_answer": "A",
        "explanation": "|\u27e8u, v\u27e9| \u2264 ||u|| ||v|| with equality if and only if u and v are linearly dependent."
    },
    {
        "id": 93,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If A is a 2x2 matrix with Trace(A) = 5 and det(A) = 6, its eigenvalues are:",
        "options": [
            "(A) 1 and 4",
            "(B) 2 and 3",
            "(C) -2 and -3",
            "(D) 5 and 6"
        ],
        "correct_answer": "B",
        "explanation": "Characteristic eq: \u03bb^2 - Trace(A)\u03bb + det(A) = \u03bb^2 - 5\u03bb + 6 = 0 => (\u03bb - 2)(\u03bb - 3) = 0 => \u03bb = 2, 3."
    },
    {
        "id": 94,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If A has eigenvalue \u03bb with eigenvector v, then (A + cI) has:",
        "options": [
            "(A) Eigenvalue \u03bb with vector cv",
            "(B) Eigenvalue (\u03bb + c) with eigenvector v",
            "(C) Eigenvalue c\u03bb",
            "(D) Different eigenvectors"
        ],
        "correct_answer": "B",
        "explanation": "(A + cI)v = Av + cv = \u03bbv + cv = (\u03bb + c)v."
    },
    {
        "id": 95,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "For any real matrix A, the matrix A^T A is ALWAYS:",
        "options": [
            "(A) Skew-symmetric",
            "(B) Symmetric and positive semi-definite",
            "(C) Orthogonal",
            "(D) Invertible"
        ],
        "correct_answer": "B",
        "explanation": "(A^T A)^T = A^T A (symmetric) and x^T (A^T A) x = ||Ax||^2 \u2265 0 (positive semi-definite)."
    },
    {
        "id": 96,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "In Principal Component Analysis (PCA), the principal directions are given by:",
        "options": [
            "(A) Eigenvectors of the sample covariance matrix",
            "(B) Columns of data matrix",
            "(C) Means of features",
            "(D) QR decomposition of data"
        ],
        "correct_answer": "A",
        "explanation": "PCA finds directions of maximum variance, which are eigenvectors of the sample covariance matrix."
    },
    {
        "id": 97,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "Two matrices A and B are similar (B = P^{-1} A P) if and only if they share the same:",
        "options": [
            "(A) Eigenvectors",
            "(B) Characteristic polynomial and eigenvalues",
            "(C) Column space",
            "(D) Inverse"
        ],
        "correct_answer": "B",
        "explanation": "Similar matrices represent the same linear transformation in different bases, preserving eigenvalues, trace, and determinant."
    },
    {
        "id": 98,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If quadratic form Q(x, y) = 2x^2 + 4xy + 5y^2, its symmetric matrix representation is:",
        "options": [
            "(A) [[2, 4], [4, 5]]",
            "(B) [[2, 2], [2, 5]]",
            "(C) [[2, 0], [0, 5]]",
            "(D) [[4, 2], [2, 5]]"
        ],
        "correct_answer": "B",
        "explanation": "The cross term 4xy is split equally into off-diagonals: a_{12} = a_{21} = 2. [[2, 2], [2, 5]]."
    },
    {
        "id": 99,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "Using Sylvester's criterion, a 2x2 symmetric matrix [[a, b], [b, c]] is positive definite if:",
        "options": [
            "(A) a > 0 and ac - b^2 > 0",
            "(B) a > 0 and b > 0",
            "(C) ac > 0",
            "(D) a + c > 0"
        ],
        "correct_answer": "A",
        "explanation": "Leading principal minors must be strictly positive: M_1 = a > 0, M_2 = ac - b^2 = det > 0."
    },
    {
        "id": 100,
        "subject": "Linear Algebra",
        "chapter": "Eigenvalues & Matrix Decompositions",
        "question": "If \u03bb_1 \u2265 \u03bb_2 \u2265 ... \u2265 \u03bb_n are eigenvalues of symmetric A, Rayleigh quotient R(x) = (x^T A x)/(x^T x) satisfies:",
        "options": [
            "(A) R(x) = \u03bb_1 always",
            "(B) \u03bb_n \u2264 R(x) \u2264 \u03bb_1",
            "(C) R(x) \u2265 0 always",
            "(D) R(x) \u2264 \u03bb_n"
        ],
        "correct_answer": "B",
        "explanation": "Rayleigh-Ritz theorem bounds Rayleigh quotient between minimum and maximum eigenvalues."
    },
    {
        "id": 101,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "What is lim_{x -> 0} (sin 3x) / x?",
        "options": [
            "(A) 0",
            "(B) 1",
            "(C) 3",
            "(D) Does not exist"
        ],
        "correct_answer": "C",
        "explanation": "Using standard limit lim_{u->0} (sin u)/u = 1: lim 3 * (sin 3x)/(3x) = 3 * 1 = 3 (or by L'Hopital: cos(3x)*3 / 1 = 3)."
    },
    {
        "id": 102,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "What is lim_{x -> 0} (e^{2x} - 1) / x?",
        "options": [
            "(A) 0",
            "(B) 1",
            "(C) 2",
            "(D) \u221e"
        ],
        "correct_answer": "C",
        "explanation": "By L'Hopital rule: derivative of numerator is 2e^{2x}, denominator is 1. Evaluated at 0 gives 2(1)/1 = 2."
    },
    {
        "id": 103,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "If f(x) = |x|, at x = 0 the function is:",
        "options": [
            "(A) Discontinuous",
            "(B) Continuous but not differentiable",
            "(C) Differentiable with f'(0) = 0",
            "(D) Unbounded"
        ],
        "correct_answer": "B",
        "explanation": "Left derivative is -1, right derivative is +1. Since left and right derivatives differ, f is continuous but not differentiable at 0."
    },
    {
        "id": 104,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "Rolle's theorem states that if f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there exists c in (a, b) where:",
        "options": [
            "(A) f(c) = 0",
            "(B) f'(c) = 0",
            "(C) f''(c) = 0",
            "(D) f(c) = (f(b)-f(a))/(b-a)"
        ],
        "correct_answer": "B",
        "explanation": "Rolle's theorem guarantees at least one stationary point c where the tangent is horizontal: f'(c) = 0."
    },
    {
        "id": 105,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "Lagrange's Mean Value Theorem states there exists c in (a, b) such that f'(c) equals:",
        "options": [
            "(A) 0",
            "(B) (f(b) - f(a)) / (b - a)",
            "(C) (f(b) + f(a)) / 2",
            "(D) f(b) - f(a)"
        ],
        "correct_answer": "B",
        "explanation": "MVT guarantees instantaneous rate of change equals average rate of change over [a, b]."
    },
    {
        "id": 106,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "The first two non-zero terms of Taylor series of f(x) = e^x around x = 0 are:",
        "options": [
            "(A) 1 + x",
            "(B) x + x^2",
            "(C) 1 + x^2/2",
            "(D) 1 - x"
        ],
        "correct_answer": "A",
        "explanation": "e^x = 1 + x + x^2/2! + x^3/3! + ... First two terms are 1 + x."
    },
    {
        "id": 107,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "A function f(x) has a local minimum at x = c if:",
        "options": [
            "(A) f'(c) = 0 and f''(c) > 0",
            "(B) f'(c) = 0 and f''(c) < 0",
            "(C) f'(c) > 0",
            "(D) f''(c) = 0"
        ],
        "correct_answer": "A",
        "explanation": "Second derivative test: f'(c) = 0 and positive curvature (concave up, f''(c) > 0) indicates a local minimum."
    },
    {
        "id": 108,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "An inflection point of a twice differentiable function f(x) occurs where:",
        "options": [
            "(A) f'(x) = 0",
            "(B) f''(x) changes sign",
            "(C) f(x) = 0",
            "(D) f'(x) is undefined"
        ],
        "correct_answer": "B",
        "explanation": "An inflection point is a point on a curve at which the concavity changes sign (f''(x) crosses zero)."
    },
    {
        "id": 109,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "The gradient vector \u2207f of a scalar function f(x, y) points in the direction of:",
        "options": [
            "(A) Zero change",
            "(B) Steepest rate of increase",
            "(C) Steepest rate of decrease",
            "(D) Tangent to contour curve"
        ],
        "correct_answer": "B",
        "explanation": "\u2207f points in the direction of maximum rate of increase, and its magnitude ||\u2207f|| is the maximum rate."
    },
    {
        "id": 110,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "The directional derivative D_u f(x_0) in direction of unit vector u is given by:",
        "options": [
            "(A) \u2207f \u00b7 u",
            "(B) \u2207f \u00d7 u",
            "(C) ||\u2207f|| / ||u||",
            "(D) \u2207f + u"
        ],
        "correct_answer": "A",
        "explanation": "D_u f(x_0) = \u2207f(x_0) \u00b7 u = ||\u2207f|| cos \u03b8."
    },
    {
        "id": 111,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "At any point on a level curve f(x, y) = c, the gradient vector \u2207f is:",
        "options": [
            "(A) Parallel to tangent line",
            "(B) Orthogonal (perpendicular) to tangent line",
            "(C) In direction of contour",
            "(D) Zero"
        ],
        "correct_answer": "B",
        "explanation": "The gradient vector is strictly normal (perpendicular) to the level curve / contour surface."
    },
    {
        "id": 112,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "Let f(x, y) = x^2 y + 3y. The partial derivative \u2202f/\u2202x at (1, 2) is:",
        "options": [
            "(A) 4",
            "(B) 7",
            "(C) 2",
            "(D) 5"
        ],
        "correct_answer": "A",
        "explanation": "\u2202f/\u2202x = 2xy. At (1, 2), \u2202f/\u2202x = 2(1)(2) = 4."
    },
    {
        "id": 113,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "For f(x, y) = x^2 y + 3y, the partial derivative \u2202f/\u2202y at (1, 2) is:",
        "options": [
            "(A) 4",
            "(B) 1",
            "(C) 4",
            "(D) 4"
        ],
        "correct_answer": "A",
        "explanation": "\u2202f/\u2202y = x^2 + 3. At (1, 2), 1^2 + 3 = 4."
    },
    {
        "id": 114,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "Clairaut's theorem states that mixed second partial derivatives \u2202^2 f / (\u2202x \u2202y) and \u2202^2 f / (\u2202y \u2202x) are equal if:",
        "options": [
            "(A) f is a polynomial",
            "(B) Mixed partials are continuous",
            "(C) \u2207f = 0",
            "(D) f is convex"
        ],
        "correct_answer": "B",
        "explanation": "Schwarz / Clairaut's theorem guarantees equality when second partial derivatives are continuous."
    },
    {
        "id": 115,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "The equation of the tangent plane to surface z = f(x, y) at (x_0, y_0, z_0) is:",
        "options": [
            "(A) z - z_0 = f_x(x - x_0) + f_y(y - y_0)",
            "(B) z = f_x x + f_y y",
            "(C) (x - x_0)/f_x = (y - y_0)/f_y",
            "(D) z - z_0 = f_x f_y"
        ],
        "correct_answer": "A",
        "explanation": "Tangent plane linear approximation: z - z_0 = \u2202f/\u2202x (x - x_0) + \u2202f/\u2202y (y - y_0)."
    },
    {
        "id": 116,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "If z = f(x, y) where x = g(t) and y = h(t), the chain rule gives dz/dt as:",
        "options": [
            "(A) \u2202f/\u2202x + \u2202f/\u2202y",
            "(B) (\u2202f/\u2202x)(dx/dt) + (\u2202f/\u2202y)(dy/dt)",
            "(C) (\u2202f/\u2202x)(dy/dt)",
            "(D) (dx/dt)(dy/dt)"
        ],
        "correct_answer": "B",
        "explanation": "Total derivative chain rule: dz/dt = (\u2202f/\u2202x)(dx/dt) + (\u2202f/\u2202y)(dy/dt)."
    },
    {
        "id": 117,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "The total differential df of f(x, y) is given by:",
        "options": [
            "(A) (\u2202f/\u2202x) dx + (\u2202f/\u2202y) dy",
            "(B) (\u2202f/\u2202x) dy + (\u2202f/\u2202y) dx",
            "(C) f dx dy",
            "(D) (\u2202f/\u2202x)(\u2202f/\u2202y)"
        ],
        "correct_answer": "A",
        "explanation": "df = (\u2202f/\u2202x) dx + (\u2202f/\u2202y) dy."
    },
    {
        "id": 118,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "For f(x, y) = x^2 + y^2, what is the directional derivative at (1, 1) in direction of v = [1, 0]^T?",
        "options": [
            "(A) 1",
            "(B) 2",
            "(C) 4",
            "(D) 0"
        ],
        "correct_answer": "B",
        "explanation": "\u2207f = [2x, 2y]^T = [2, 2]^T. Unit vector u = [1, 0]^T. D_u f = \u2207f \u00b7 u = 2(1) + 2(0) = 2."
    },
    {
        "id": 119,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "What is the maximum rate of increase of f(x, y) = 3x^2 + 4y^2 at point (1, 1)?",
        "options": [
            "(A) 7",
            "(B) 10",
            "(C) 14",
            "(D) 48"
        ],
        "correct_answer": "B",
        "explanation": "\u2207f = [6x, 8y]^T. At (1, 1), \u2207f = [6, 8]^T. Max rate = ||\u2207f|| = \u221a(6^2 + 8^2) = \u221a100 = 10."
    },
    {
        "id": 120,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "A critical point (x_0, y_0) of a differentiable multivariable function f satisfies:",
        "options": [
            "(A) f(x_0, y_0) = 0",
            "(B) \u2207f(x_0, y_0) = [0, 0]^T",
            "(C) \u2202^2f/\u2202x^2 = 0",
            "(D) f is discontinuous"
        ],
        "correct_answer": "B",
        "explanation": "Critical points occur where the gradient vector is zero (all partial derivatives vanish)."
    },
    {
        "id": 121,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "What is lim_{x -> \u221e} (1 + 1/x)^x?",
        "options": [
            "(A) 1",
            "(B) 0",
            "(C) e",
            "(D) \u221e"
        ],
        "correct_answer": "C",
        "explanation": "Euler's number definition: lim_{x -> \u221e} (1 + 1/x)^x = e \u2248 2.718."
    },
    {
        "id": 122,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "Derivative of f(x) = ln(x^2 + 1) is:",
        "options": [
            "(A) 1 / (x^2 + 1)",
            "(B) 2x / (x^2 + 1)",
            "(C) 2x ln(x^2 + 1)",
            "(D) x / (x^2 + 1)"
        ],
        "correct_answer": "B",
        "explanation": "By chain rule: (1 / (x^2 + 1)) * d/dx(x^2 + 1) = 2x / (x^2 + 1)."
    },
    {
        "id": 123,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "If f(x) = x^3 - 3x, the critical points are at x = :",
        "options": [
            "(A) 0 and 1",
            "(B) +1 and -1",
            "(C) 0 and 3",
            "(D) \u00b13"
        ],
        "correct_answer": "B",
        "explanation": "f'(x) = 3x^2 - 3 = 0 => 3(x^2 - 1) = 0 => x = \u00b11."
    },
    {
        "id": 124,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "For f(x) = x^3 - 3x, what is the nature of critical point x = 1?",
        "options": [
            "(A) Local maximum",
            "(B) Local minimum",
            "(C) Inflection point",
            "(D) Saddle point"
        ],
        "correct_answer": "B",
        "explanation": "f''(x) = 6x. At x = 1, f''(1) = 6 > 0, which corresponds to a local minimum."
    },
    {
        "id": 125,
        "subject": "Calculus and Optimization",
        "chapter": "Functions and Differentiation",
        "question": "L'Hopital's rule can be applied directly to which indeterminate forms?",
        "options": [
            "(A) 0/0 and \u221e/\u221e",
            "(B) 0 * \u221e",
            "(C) 1^\u221e",
            "(D) 0^0"
        ],
        "correct_answer": "A",
        "explanation": "L'Hopital's rule applies directly to ratios 0/0 and \u00b1\u221e/\u00b1\u221e (other forms must be transformed to ratios first)."
    },
    {
        "id": 126,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "The Hessian matrix H of a twice-differentiable multivariable function f: R^n -> R contains:",
        "options": [
            "(A) First partial derivatives",
            "(B) Second-order partial derivatives H_ij = \u2202^2f / (\u2202x_i \u2202x_j)",
            "(C) Eigenvalues only",
            "(D) Gradient norms"
        ],
        "correct_answer": "B",
        "explanation": "H is the n x n square matrix of second-order partial derivatives."
    },
    {
        "id": 127,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "At a critical point x* where \u2207f(x*) = 0, if the Hessian H(x*) is positive definite, x* is a:",
        "options": [
            "(A) Local minimum",
            "(B) Local maximum",
            "(C) Saddle point",
            "(D) Inconclusive"
        ],
        "correct_answer": "A",
        "explanation": "Positive definite Hessian (all eigenvalues > 0) means positive curvature in all directions: local minimum."
    },
    {
        "id": 128,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "At a critical point x* where \u2207f(x*) = 0, if the Hessian H(x*) is negative definite, x* is a:",
        "options": [
            "(A) Local minimum",
            "(B) Local maximum",
            "(C) Saddle point",
            "(D) Inconclusive"
        ],
        "correct_answer": "B",
        "explanation": "Negative definite Hessian (all eigenvalues < 0) means negative curvature in all directions: local maximum."
    },
    {
        "id": 129,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "At a critical point x*, if the Hessian H(x*) has both positive and negative eigenvalues, x* is a:",
        "options": [
            "(A) Local minimum",
            "(B) Local maximum",
            "(C) Saddle point",
            "(D) Global minimum"
        ],
        "correct_answer": "C",
        "explanation": "Indefinite Hessian (both positive and negative eigenvalues) defines a saddle point."
    },
    {
        "id": 130,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "A set S in R^n is convex if for all x, y in S and \u03b8 in [0, 1]:",
        "options": [
            "(A) \u03b8x + (1 - \u03b8)y \u2208 S",
            "(B) x + y \u2208 S",
            "(C) \u03b8x \u2208 S",
            "(D) ||x - y|| \u2264 1"
        ],
        "correct_answer": "A",
        "explanation": "A set is convex if the line segment connecting any two points in S lies entirely within S."
    },
    {
        "id": 131,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Which of the following sets is NOT convex?",
        "options": [
            "(A) The unit ball {x : ||x|| \u2264 1}",
            "(B) A hyperplane {x : a^T x = b}",
            "(C) The unit circle {x : ||x|| = 1}",
            "(D) A half-space {x : a^T x \u2264 b}"
        ],
        "correct_answer": "C",
        "explanation": "The boundary circle contains (1,0) and (-1,0), but their midpoint (0,0) is not on the circle."
    },
    {
        "id": 132,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "A twice differentiable function f: R^n -> R is convex if and only if its Hessian H(x) is:",
        "options": [
            "(A) Positive semi-definite for all x",
            "(B) Strictly negative",
            "(C) Diagonal",
            "(D) Zero"
        ],
        "correct_answer": "A",
        "explanation": "Second-order condition for convexity: H(x) \u2ab0 0 (positive semi-definite) for all x in the domain."
    },
    {
        "id": 133,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "A fundamental property of convex functions is that:",
        "options": [
            "(A) Every local minimum is a global minimum",
            "(B) They have no critical points",
            "(C) They must be strictly linear",
            "(D) Hessian is always identity"
        ],
        "correct_answer": "A",
        "explanation": "For any convex function on a convex set, any local minimum is guaranteed to be a global minimum."
    },
    {
        "id": 134,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "If f is strictly convex, how many global minimizers can f have?",
        "options": [
            "(A) Infinitely many",
            "(B) At most one (unique)",
            "(C) Exactly two",
            "(D) None"
        ],
        "correct_answer": "B",
        "explanation": "Strict convexity guarantees that if a global minimizer exists, it is strictly unique."
    },
    {
        "id": 135,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Jensen's inequality states that for a convex function f and random variable X:",
        "options": [
            "(A) f(E[X]) \u2264 E[f(X)]",
            "(B) f(E[X]) \u2265 E[f(X)]",
            "(C) f(E[X]) = E[f(X)]",
            "(D) E[f(X)] = 0"
        ],
        "correct_answer": "A",
        "explanation": "For any convex function f, secant line lies above curve: f(E[X]) \u2264 E[f(X)]."
    },
    {
        "id": 136,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "The Gradient Descent parameter update rule with step size (learning rate) \u03b3 is:",
        "options": [
            "(A) x^{(t+1)} = x^{(t)} + \u03b3 \u2207f(x^{(t)})",
            "(B) x^{(t+1)} = x^{(t)} - \u03b3 \u2207f(x^{(t)})",
            "(C) x^{(t+1)} = \u03b3 x^{(t)}",
            "(D) x^{(t+1)} = -\u2207f(x^{(t)})"
        ],
        "correct_answer": "B",
        "explanation": "Gradient descent moves in the direction opposite to the gradient: x^{(t+1)} = x^{(t)} - \u03b3 \u2207f(x^{(t)})."
    },
    {
        "id": 137,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "If the learning rate \u03b3 in gradient descent is chosen too large, the algorithm may:",
        "options": [
            "(A) Converge instantaneously",
            "(B) Oscillate and diverge (overshoot)",
            "(C) Get stuck at the start",
            "(D) Become Newton's method"
        ],
        "correct_answer": "B",
        "explanation": "Excessively large learning rates cause overshooting across valley walls, leading to divergence."
    },
    {
        "id": 138,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Newton's optimization method uses which update step for multivariable optimization?",
        "options": [
            "(A) x - \u03b3 \u2207f",
            "(B) x - [H(x)]^{-1} \u2207f(x)",
            "(C) x - H(x) \u2207f(x)",
            "(D) x + [H(x)]^{-1}"
        ],
        "correct_answer": "B",
        "explanation": "Newton-Raphson uses second-order quadratic approximation: \u0394x = -H^{-1} \u2207f."
    },
    {
        "id": 139,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Compared to Gradient Descent, Newton's method has:",
        "options": [
            "(A) Slower convergence",
            "(B) Quadratic convergence rate near the minimum",
            "(C) O(n) per-iteration cost",
            "(D) No need for second derivatives"
        ],
        "correct_answer": "B",
        "explanation": "Newton's method achieves quadratic convergence near the optimum, but requires O(n^3) Hessian inversion per step."
    },
    {
        "id": 140,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "In optimization with equality constraint g(x) = 0, the method of Lagrange Multipliers solves:",
        "options": [
            "(A) \u2207f(x) + \u03bb \u2207g(x) = 0 and g(x) = 0",
            "(B) \u2207f(x) = \u2207g(x)",
            "(C) f(x) + g(x) = 0",
            "(D) \u03bb = 0"
        ],
        "correct_answer": "A",
        "explanation": "At constrained optimum, gradients of objective and constraint must be collinear: \u2207f + \u03bb \u2207g = 0."
    },
    {
        "id": 141,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "The Karush-Kuhn-Tucker (KKT) conditions generalize Lagrange multipliers to handle:",
        "options": [
            "(A) Non-differentiable functions",
            "(B) Inequality constraints g_i(x) \u2264 0",
            "(C) Discrete integer variables",
            "(D) Complex numbers"
        ],
        "correct_answer": "B",
        "explanation": "KKT conditions provide necessary conditions for optimality in problems with inequality constraints."
    },
    {
        "id": 142,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "The KKT complementary slackness condition for constraint g_i(x) \u2264 0 with dual multiplier \u03bb_i is:",
        "options": [
            "(A) \u03bb_i + g_i(x) = 0",
            "(B) \u03bb_i * g_i(x) = 0 with \u03bb_i \u2265 0",
            "(C) \u03bb_i / g_i(x) = 1",
            "(D) \u03bb_i > 0 always"
        ],
        "correct_answer": "B",
        "explanation": "Complementary slackness requires \u03bb_i g_i(x) = 0: either constraint is active (g_i = 0) or multiplier is zero (\u03bb_i = 0)."
    },
    {
        "id": 143,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "In convex optimization, if strong duality holds, the duality gap is:",
        "options": [
            "(A) 1",
            "(B) 0",
            "(C) Strictly positive",
            "(D) Negative"
        ],
        "correct_answer": "B",
        "explanation": "Strong duality means optimal primal objective value equals optimal dual objective value (duality gap = 0)."
    },
    {
        "id": 144,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Slater's condition is a constraint qualification that guarantees:",
        "options": [
            "(A) Non-convexity",
            "(B) Strong duality for convex optimization problems",
            "(C) Zero gradient everywhere",
            "(D) Nilpotency"
        ],
        "correct_answer": "B",
        "explanation": "Slater's condition (existence of a strictly feasible point) guarantees strong duality in convex optimization."
    },
    {
        "id": 145,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Momentum in gradient descent helps to:",
        "options": [
            "(A) Accelerate in consistent directions and dampen oscillations in ravines",
            "(B) Eliminate the need for gradients",
            "(C) Double the learning rate",
            "(D) Invert the Hessian"
        ],
        "correct_answer": "A",
        "explanation": "Momentum adds a fraction of previous update: v_t = \u03b2 v_{t-1} + \u03b3 \u2207f, smoothing path through steep ravines."
    },
    {
        "id": 146,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "Stochastic Gradient Descent (SGD) updates parameters using:",
        "options": [
            "(A) The full dataset gradient",
            "(B) Gradient evaluated on a single sample or mini-batch",
            "(C) Second derivatives",
            "(D) A random walk"
        ],
        "correct_answer": "B",
        "explanation": "SGD estimates gradient from a single sample or mini-batch, reducing per-iteration computation from O(N) to O(B)."
    },
    {
        "id": 147,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "For f(x, y) = x^2 + 2y^2, the Hessian matrix is:",
        "options": [
            "(A) [[1, 0], [0, 2]]",
            "(B) [[2, 0], [0, 4]]",
            "(C) [[2, 2], [2, 4]]",
            "(D) [[x, 0], [0, y]]"
        ],
        "correct_answer": "B",
        "explanation": "\u2202^2f/\u2202x^2 = 2, \u2202^2f/\u2202y^2 = 4, cross partials = 0. H = [[2, 0], [0, 4]]."
    },
    {
        "id": 148,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "For f(x, y) = x^2 - y^2, the origin (0, 0) is a:",
        "options": [
            "(A) Local minimum",
            "(B) Local maximum",
            "(C) Saddle point",
            "(D) Non-critical point"
        ],
        "correct_answer": "C",
        "explanation": "Hessian is [[2, 0], [0, -2]] with eigenvalues +2 and -2. Since eigenvalues have opposite signs, (0,0) is a saddle point."
    },
    {
        "id": 149,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "In L1 regularization (Lasso), the penalty term added to loss is:",
        "options": [
            "(A) \u03bb \u2211 w_i^2",
            "(B) \u03bb \u2211 |w_i|",
            "(C) \u03bb max |w_i|",
            "(D) \u03bb / ||w||"
        ],
        "correct_answer": "B",
        "explanation": "L1 regularization adds \u03bb ||w||_1 = \u03bb \u2211 |w_i|, promoting sparse weight solutions."
    },
    {
        "id": 150,
        "subject": "Calculus and Optimization",
        "chapter": "Optimization Techniques",
        "question": "In L2 regularization (Ridge), the penalty term added to loss is:",
        "options": [
            "(A) \u03bb \u2211 |w_i|",
            "(B) \u03bb \u2211 w_i^2",
            "(C) \u03bb \u220f w_i",
            "(D) \u03bb ln(w)"
        ],
        "correct_answer": "B",
        "explanation": "L2 regularization adds \u03bb ||w||_2^2 = \u03bb \u2211 w_i^2, shrinking weights smoothly towards zero."
    },
    {
        "id": 151,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "Which of the following built-in Python data types is IMMUTABLE?",
        "options": [
            "(A) List",
            "(B) Dictionary",
            "(C) Tuple",
            "(D) Set"
        ],
        "correct_answer": "C",
        "explanation": "Tuples, strings, numbers, and frozensets are immutable in Python. Lists, dictionaries, and sets are mutable."
    },
    {
        "id": 152,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the output of `bool([])`, `bool([0])`, `bool('')` in Python?",
        "options": [
            "(A) False, True, False",
            "(B) False, False, False",
            "(C) True, True, False",
            "(D) False, True, True"
        ],
        "correct_answer": "A",
        "explanation": "Empty collections (`[]`, `''`) evaluate to False. Non-empty collections (`[0]`) evaluate to True."
    },
    {
        "id": 153,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What does `func(a, L=[])` suffer from if L is modified inside the function?",
        "options": [
            "(A) Syntax error",
            "(B) Default argument is evaluated once at definition time and shared across calls",
            "(C) Memory leak",
            "(D) Out of scope error"
        ],
        "correct_answer": "B",
        "explanation": "Default parameter values are evaluated once when the function definition is executed, creating a shared mutable state."
    },
    {
        "id": 154,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the time complexity of looking up a key in a Python dictionary on average?",
        "options": [
            "(A) O(1)",
            "(B) O(log n)",
            "(C) O(n)",
            "(D) O(n log n)"
        ],
        "correct_answer": "A",
        "explanation": "Python dictionaries are implemented using hash tables, giving average O(1) time complexity for lookups."
    },
    {
        "id": 155,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What keyword is used in Python to turn a normal function into a generator?",
        "options": [
            "(A) return",
            "(B) yield",
            "(C) generate",
            "(D) async"
        ],
        "correct_answer": "B",
        "explanation": "The `yield` statement suspends function execution and returns an iterator generator object."
    },
    {
        "id": 156,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the output of `[x**2 for x in range(5) if x % 2 == 1]`?",
        "options": [
            "(A) [1, 9]",
            "(B) [0, 4, 16]",
            "(C) [1, 4, 9]",
            "(D) [1, 9, 25]"
        ],
        "correct_answer": "A",
        "explanation": "Odd numbers in range(5) are 1 and 3. Their squares are 1 and 9."
    },
    {
        "id": 157,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "In Python, arguments are passed by:",
        "options": [
            "(A) Value only",
            "(B) Reference only",
            "(C) Assignment (Object Reference)",
            "(D) Pointer"
        ],
        "correct_answer": "C",
        "explanation": "Python uses 'call-by-object-reference'. Variable names are bound to objects; modifying mutable objects affects the caller."
    },
    {
        "id": 158,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the difference between `copy.copy(x)` and `copy.deepcopy(x)`?",
        "options": [
            "(A) deepcopy is faster",
            "(B) copy creates shallow copy; deepcopy recursively copies nested objects",
            "(C) copy works only on lists",
            "(D) deepcopy freezes object"
        ],
        "correct_answer": "B",
        "explanation": "Shallow copy copies the outer object but references nested objects; deepcopy recursively duplicates all child objects."
    },
    {
        "id": 159,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the result of `type(lambda x: x + 1)` in Python?",
        "options": [
            "(A) <class 'function'>",
            "(B) <class 'lambda'>",
            "(C) <class 'expression'>",
            "(D) <class 'int'>"
        ],
        "correct_answer": "A",
        "explanation": "A lambda expression creates a first-class function object of type `function`."
    },
    {
        "id": 160,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What does the `@decorator` syntax above a function definition `def f():` do?",
        "options": [
            "(A) Calls f immediately",
            "(B) Replaces f with decorator(f)",
            "(C) Compiles f to C",
            "(D) Deletes f"
        ],
        "correct_answer": "B",
        "explanation": "`@decorator` is syntactic sugar for `f = decorator(f)`."
    },
    {
        "id": 161,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What block in a try-except structure is ALWAYS executed, whether an exception occurs or not?",
        "options": [
            "(A) catch",
            "(B) else",
            "(C) finally",
            "(D) always"
        ],
        "correct_answer": "C",
        "explanation": "The `finally` block is guaranteed to execute regardless of whether an exception was raised or handled."
    },
    {
        "id": 162,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "In Python, what is the Method Resolution Order (MRO) algorithm used for multiple inheritance?",
        "options": [
            "(A) Depth-first search",
            "(B) Breadth-first search",
            "(C) C3 Linearization",
            "(D) Topological Dijkstra"
        ],
        "correct_answer": "C",
        "explanation": "Python uses the C3 Linearization algorithm to determine method resolution order in complex inheritance hierarchies."
    },
    {
        "id": 163,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the result of `list(map(lambda x: x*2, [1, 2, 3]))`?",
        "options": [
            "(A) [1, 2, 3, 1, 2, 3]",
            "(B) [2, 4, 6]",
            "(C) [2, 2, 2]",
            "(D) [6]"
        ],
        "correct_answer": "B",
        "explanation": "`map` applies the lambda to each element: 1*2=2, 2*2=4, 3*2=6."
    },
    {
        "id": 164,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What does `*args` and `**kwargs` in a function signature allow?",
        "options": [
            "(A) Pointer manipulation",
            "(B) Variable number of positional and keyword arguments",
            "(C) Fast compilation",
            "(D) Global variables"
        ],
        "correct_answer": "B",
        "explanation": "`*args` collects arbitrary positional arguments into a tuple; `**kwargs` collects keyword arguments into a dictionary."
    },
    {
        "id": 165,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the output of `print('GATE'[::-1])`?",
        "options": [
            "(A) GATE",
            "(B) ETAG",
            "(C) G",
            "(D) Error"
        ],
        "correct_answer": "B",
        "explanation": "Slice syntax `[::-1]` reverses the string, producing 'ETAG'."
    },
    {
        "id": 166,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the time complexity of appending an element to a Python list on average?",
        "options": [
            "(A) O(1) amortized",
            "(B) O(n)",
            "(C) O(log n)",
            "(D) O(n^2)"
        ],
        "correct_answer": "A",
        "explanation": "Python lists are dynamic arrays with over-allocation, giving O(1) amortized append complexity."
    },
    {
        "id": 167,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What built-in function returns an iterator of tuples containing index and value?",
        "options": [
            "(A) zip()",
            "(B) enumerate()",
            "(C) range()",
            "(D) index()"
        ],
        "correct_answer": "B",
        "explanation": "`enumerate(iterable)` yields `(index, item)` pairs."
    },
    {
        "id": 168,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "In Python, what is a generator expression compared to a list comprehension?",
        "options": [
            "(A) Returns a tuple",
            "(B) Uses parentheses and generates items lazily on demand",
            "(C) Faster indexing",
            "(D) Uses more memory"
        ],
        "correct_answer": "B",
        "explanation": "Generator expressions `(x for x in data)` evaluate lazily, consuming minimal memory compared to list comprehensions."
    },
    {
        "id": 169,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What does the `is` operator compare in Python?",
        "options": [
            "(A) Value equality",
            "(B) Object identity (memory address)",
            "(C) Data type",
            "(D) Length"
        ],
        "correct_answer": "B",
        "explanation": "`is` checks if two variables point to the exact same object in memory (`id(a) == id(b)`), whereas `==` checks value equality."
    },
    {
        "id": 170,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the output of `set([1, 2, 2, 3, 1])`?",
        "options": [
            "(A) [1, 2, 3]",
            "(B) {1, 2, 3}",
            "(C) (1, 2, 3)",
            "(D) {1: 2, 3: 1}"
        ],
        "correct_answer": "B",
        "explanation": "Sets automatically eliminate duplicates, returning `{1, 2, 3}`."
    },
    {
        "id": 171,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What exception is raised when accessing a non-existent key in a Python dict with `d[k]`?",
        "options": [
            "(A) IndexError",
            "(B) KeyError",
            "(C) ValueError",
            "(D) AttributeError"
        ],
        "correct_answer": "B",
        "explanation": "Accessing an invalid key using square brackets raises `KeyError`. Using `d.get(k)` returns None instead."
    },
    {
        "id": 172,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What does `sys.getrefcount(x)` return?",
        "options": [
            "(A) Size of x in bytes",
            "(B) Reference count of object x",
            "(C) Execution time",
            "(D) Number of variables in scope"
        ],
        "correct_answer": "B",
        "explanation": "Python's garbage collector uses reference counting; `getrefcount` returns the current count of references."
    },
    {
        "id": 173,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What does `__init__` represent in a Python class?",
        "options": [
            "(A) Class destructor",
            "(B) Instance initializer constructor",
            "(C) Static method",
            "(D) Module loader"
        ],
        "correct_answer": "B",
        "explanation": "`__init__` is the instance initialization method called when a new class instance is constructed."
    },
    {
        "id": 174,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "Which module provides high-performance container alternatives like deque, defaultdict, and Counter?",
        "options": [
            "(A) itertools",
            "(B) collections",
            "(C) functools",
            "(D) array"
        ],
        "correct_answer": "B",
        "explanation": "The standard `collections` module provides specialized container datatypes."
    },
    {
        "id": 175,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Python Programming",
        "question": "What is the output of `3 * [1, 2]`?",
        "options": [
            "(A) [3, 6]",
            "(B) [1, 2, 1, 2, 1, 2]",
            "(C) [[1, 2], [1, 2], [1, 2]]",
            "(D) TypeError"
        ],
        "correct_answer": "B",
        "explanation": "Multiplying a list by integer k concatenates k copies of the list elements: `[1, 2, 1, 2, 1, 2]`."
    },
    {
        "id": 176,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "According to the Master Theorem, the solution to T(n) = 2T(n/2) + O(n) is:",
        "options": [
            "(A) O(n)",
            "(B) O(n log n)",
            "(C) O(n^2)",
            "(D) O(log n)"
        ],
        "correct_answer": "B",
        "explanation": "a = 2, b = 2, f(n) = n. Since n^{log_b a} = n^1 = f(n), Case 2 applies: T(n) = O(n log n) (Merge Sort)."
    },
    {
        "id": 177,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "According to the Master Theorem, the solution to T(n) = 4T(n/2) + O(n) is:",
        "options": [
            "(A) O(n log n)",
            "(B) O(n^2)",
            "(C) O(n^3)",
            "(D) O(2^n)"
        ],
        "correct_answer": "B",
        "explanation": "a = 4, b = 2 => n^{log_2 4} = n^2. Since f(n) = n = O(n^{2 - \u03b5}), Case 1 applies: T(n) = O(n^2)."
    },
    {
        "id": 178,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What is the worst-case time complexity of Quick Sort?",
        "options": [
            "(A) O(n log n)",
            "(B) O(n)",
            "(C) O(n^2)",
            "(D) O(log n)"
        ],
        "correct_answer": "C",
        "explanation": "When the pivot is consistently the smallest or largest element (e.g. already sorted array without random pivot), Quick Sort degrades to O(n^2)."
    },
    {
        "id": 179,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Which of the following sorting algorithms is NOT stable in its standard implementation?",
        "options": [
            "(A) Merge Sort",
            "(B) Insertion Sort",
            "(C) Quick Sort",
            "(D) Bubble Sort"
        ],
        "correct_answer": "C",
        "explanation": "Standard Quick Sort swaps non-adjacent elements over the pivot, potentially altering the relative order of equal keys."
    },
    {
        "id": 180,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What data structure is used to implement Breadth-First Search (BFS)?",
        "options": [
            "(A) Stack",
            "(B) Queue",
            "(C) Priority Queue",
            "(D) Binary Tree"
        ],
        "correct_answer": "B",
        "explanation": "BFS visits nodes level by level using a FIFO Queue."
    },
    {
        "id": 181,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What data structure is used to implement Depth-First Search (DFS)?",
        "options": [
            "(A) Stack (or recursion call stack)",
            "(B) Queue",
            "(C) Heap",
            "(D) Hash Table"
        ],
        "correct_answer": "A",
        "explanation": "DFS explores along branches to maximum depth using a LIFO Stack or recursive function call stack."
    },
    {
        "id": 182,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "In a Binary Search Tree (BST), which traversal produces values in STRICTLY ASCENDING order?",
        "options": [
            "(A) Preorder",
            "(B) Inorder",
            "(C) Postorder",
            "(D) Level order"
        ],
        "correct_answer": "B",
        "explanation": "Inorder traversal (Left, Root, Right) of a BST visits elements in strictly sorted ascending order."
    },
    {
        "id": 183,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "In a max-heap of n elements, what is the time complexity to extract the maximum element?",
        "options": [
            "(A) O(1)",
            "(B) O(log n)",
            "(C) O(n)",
            "(D) O(n log n)"
        ],
        "correct_answer": "B",
        "explanation": "Removing the root and restoring the heap invariant via heapify down takes O(log n) time."
    },
    {
        "id": 184,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Building a binary heap from an unsorted array of n elements takes:",
        "options": [
            "(A) O(n log n)",
            "(B) O(n)",
            "(C) O(n^2)",
            "(D) O(log n)"
        ],
        "correct_answer": "B",
        "explanation": "Bottom-up heap construction (Floyd's algorithm) takes linear O(n) time."
    },
    {
        "id": 185,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Dijkstra's shortest path algorithm works correctly on graphs with:",
        "options": [
            "(A) Negative edge weights",
            "(B) Negative cycles",
            "(C) Non-negative edge weights only",
            "(D) Bipartite graphs only"
        ],
        "correct_answer": "C",
        "explanation": "Dijkstra uses greedy relaxation which assumes path weights never decrease; it fails on graphs with negative weights."
    },
    {
        "id": 186,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Which algorithm finds single-source shortest paths on graphs with negative edge weights (and detects negative cycles)?",
        "options": [
            "(A) Dijkstra",
            "(B) Bellman-Ford",
            "(C) Kruskal",
            "(D) Prim"
        ],
        "correct_answer": "B",
        "explanation": "Bellman-Ford relaxes all edges |V| - 1 times and detects negative weight cycles in O(V * E) time."
    },
    {
        "id": 187,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What algorithm finds All-Pairs Shortest Paths in O(V^3) time using dynamic programming?",
        "options": [
            "(A) Floyd-Warshall",
            "(B) Dijkstra",
            "(C) Prim",
            "(D) Johnson's algorithm"
        ],
        "correct_answer": "A",
        "explanation": "Floyd-Warshall computes all-pairs shortest paths via dynamic programming recurrence in O(V^3) time."
    },
    {
        "id": 188,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Kruskal's algorithm for Minimum Spanning Tree uses which data structure for cycle detection?",
        "options": [
            "(A) Disjoint Set Union (Union-Find)",
            "(B) AVL Tree",
            "(C) Stack",
            "(D) Segment Tree"
        ],
        "correct_answer": "A",
        "explanation": "Kruskal's greedy algorithm sorts edges and uses Union-Find with path compression to prevent cycle formation."
    },
    {
        "id": 189,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "In an AVL tree, the balance factor of every node must be in the set:",
        "options": [
            "(A) {0}",
            "(B) {-1, 0, 1}",
            "(C) {-2, 0, 2}",
            "(D) Any integer"
        ],
        "correct_answer": "B",
        "explanation": "Balance factor is defined as height(left) - height(right) and must be in {-1, 0, 1} for every node in an AVL tree."
    },
    {
        "id": 190,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What is the time complexity of searching in an AVL tree with n nodes?",
        "options": [
            "(A) O(n)",
            "(B) O(log n)",
            "(C) O(1)",
            "(D) O(n log n)"
        ],
        "correct_answer": "B",
        "explanation": "Since AVL trees are strictly height-balanced, height is bounded by 1.44 log_2 n, giving O(log n) search."
    },
    {
        "id": 191,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Topological sorting is defined ONLY for:",
        "options": [
            "(A) Undirected trees",
            "(B) Directed Acyclic Graphs (DAG)",
            "(C) Complete graphs",
            "(D) Cyclic graphs"
        ],
        "correct_answer": "B",
        "explanation": "A topological sort is a linear ordering of vertices such that for every directed edge u -> v, u comes before v. Only DAGs have valid topological orderings."
    },
    {
        "id": 192,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What is the worst-case time complexity of searching for an element in an unsorted singly linked list of size n?",
        "options": [
            "(A) O(1)",
            "(B) O(log n)",
            "(C) O(n)",
            "(D) O(n^2)"
        ],
        "correct_answer": "C",
        "explanation": "In an unsorted linked list, sequential scan from head to tail takes O(n) time."
    },
    {
        "id": 193,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What is the time complexity of the 0/1 Knapsack dynamic programming algorithm with n items and capacity W?",
        "options": [
            "(A) O(n)",
            "(B) O(2^n)",
            "(C) O(n * W) pseudo-polynomial",
            "(D) O(n log W)"
        ],
        "correct_answer": "C",
        "explanation": "The standard 2D table approach fills an n x W matrix, running in O(n * W) pseudo-polynomial time."
    },
    {
        "id": 194,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "The Longest Common Subsequence (LCS) of strings 'ABCBDAB' and 'BDCABA' has length:",
        "options": [
            "(A) 3",
            "(B) 4",
            "(C) 5",
            "(D) 6"
        ],
        "correct_answer": "B",
        "explanation": "A common subsequence of maximal length is 'BCBA' or 'BDAB', which has length 4."
    },
    {
        "id": 195,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "A stack can be used for which of the following operations?",
        "options": [
            "(A) Infix to Postfix expression conversion",
            "(B) BFS graph traversal",
            "(C) FIFO job scheduling",
            "(D) Binary search"
        ],
        "correct_answer": "A",
        "explanation": "Stacks handle operator precedence and parenthesis matching in infix-to-postfix translation."
    },
    {
        "id": 196,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "In a circular queue implemented with array of size N, the full condition with one empty slot preserved is:",
        "options": [
            "(A) front == rear",
            "(B) (rear + 1) % N == front",
            "(C) rear == N - 1",
            "(D) front == 0"
        ],
        "correct_answer": "B",
        "explanation": "`(rear + 1) % N == front` distinguishes queue full from queue empty (`front == rear`)."
    },
    {
        "id": 197,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "What is the maximum number of nodes in a binary tree of height h (where a tree with single root has height 0)?",
        "options": [
            "(A) 2^h",
            "(B) 2^{h+1} - 1",
            "(C) 2^{h-1}",
            "(D) h^2"
        ],
        "correct_answer": "B",
        "explanation": "Summing maximum nodes per level: \u2211_{i=0}^h 2^i = 2^{h+1} - 1."
    },
    {
        "id": 198,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "In a complete undirected graph with n vertices, how many edges are there?",
        "options": [
            "(A) n",
            "(B) n(n - 1)",
            "(C) n(n - 1) / 2",
            "(D) n^2"
        ],
        "correct_answer": "C",
        "explanation": "Every pair of vertices has an edge: C(n, 2) = n(n - 1) / 2."
    },
    {
        "id": 199,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "Which data structure is optimal for implementing a Priority Queue?",
        "options": [
            "(A) Linked List",
            "(B) Binary Heap",
            "(C) Stack",
            "(D) Hash Table"
        ],
        "correct_answer": "B",
        "explanation": "Binary Heaps provide O(log n) insertions and O(log n) extract-min/max operations."
    },
    {
        "id": 200,
        "subject": "Programming, Data Structures and Algorithms",
        "chapter": "Data Structures & Algorithms",
        "question": "If an algorithm runs in T(n) = 8T(n/2) + O(n^2), its asymptotic complexity is:",
        "options": [
            "(A) O(n^2)",
            "(B) O(n^3)",
            "(C) O(n log n)",
            "(D) O(2^n)"
        ],
        "correct_answer": "B",
        "explanation": "a = 8, b = 2 => n^{log_2 8} = n^3. Since f(n) = n^2 = O(n^{3 - 1}), Case 1 applies: T(n) = O(n^3)."
    },
    {
        "id": 201,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In an Entity-Relationship (ER) model, a weak entity set is identified by:",
        "options": [
            "(A) Its own primary key",
            "(B) A discriminator (partial key) and identifying relationship with a strong entity",
            "(C) Foreign key only",
            "(D) Multi-valued attribute"
        ],
        "correct_answer": "B",
        "explanation": "Weak entity sets lack a primary key and depend on an identifying strong entity set plus a discriminator."
    },
    {
        "id": 202,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In relational algebra, which operator performs a projection on specific attributes?",
        "options": [
            "(A) \u03c3 (sigma)",
            "(B) \u03c0 (pi)",
            "(C) \u2a1d (bowtie)",
            "(D) \u03c1 (rho)"
        ],
        "correct_answer": "B",
        "explanation": "\u03c0 (pi) is the projection operator (selects columns); \u03c3 (sigma) selects tuples (rows)."
    },
    {
        "id": 203,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In relational algebra, the selection operator \u03c3 corresponds to which SQL clause?",
        "options": [
            "(A) SELECT",
            "(B) WHERE",
            "(C) GROUP BY",
            "(D) ORDER BY"
        ],
        "correct_answer": "B",
        "explanation": "\u03c3 filters rows based on a predicate, corresponding to SQL `WHERE` clause."
    },
    {
        "id": 204,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What is the result of natural join R \u2a1d S if relations R and S have NO common attributes?",
        "options": [
            "(A) Empty relation",
            "(B) Cartesian product R \u00d7 S",
            "(C) Union R \u222a S",
            "(D) Difference R - S"
        ],
        "correct_answer": "B",
        "explanation": "When R and S share no common attributes, natural join degenerates into Cartesian product R \u00d7 S."
    },
    {
        "id": 205,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What is the logical order of execution of clauses in a standard SQL SELECT query?",
        "options": [
            "(A) SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY",
            "(B) FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY",
            "(C) WHERE, FROM, SELECT, GROUP BY",
            "(D) FROM, SELECT, WHERE, ORDER BY"
        ],
        "correct_answer": "B",
        "explanation": "Logical execution order is: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY."
    },
    {
        "id": 206,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In SQL, what is the result of `WHERE salary = NULL`?",
        "options": [
            "(A) Matches tuples with NULL",
            "(B) Evaluates to UNKNOWN (matches no tuples)",
            "(C) Syntax error",
            "(D) Matches all tuples"
        ],
        "correct_answer": "B",
        "explanation": "NULL comparisons with `=` evaluate to UNKNOWN in three-valued logic. One must use `IS NULL`."
    },
    {
        "id": 207,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What does `COUNT(*)` in SQL count?",
        "options": [
            "(A) Only non-null attribute values",
            "(B) Total number of rows including NULLs",
            "(C) Distinct values",
            "(D) Columns in table"
        ],
        "correct_answer": "B",
        "explanation": "`COUNT(*)` counts all rows in the group/table, whereas `COUNT(column)` ignores NULL values."
    },
    {
        "id": 208,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What SQL clause filters groups AFTER aggregation has taken place?",
        "options": [
            "(A) WHERE",
            "(B) HAVING",
            "(C) FILTER",
            "(D) GROUP BY"
        ],
        "correct_answer": "B",
        "explanation": "`HAVING` filters groups produced by `GROUP BY`. `WHERE` filters rows before grouping."
    },
    {
        "id": 209,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "Which SQL join returns all rows from the left table, and matched rows from the right table (filling NULLs for unequals)?",
        "options": [
            "(A) INNER JOIN",
            "(B) LEFT OUTER JOIN",
            "(C) RIGHT OUTER JOIN",
            "(D) CROSS JOIN"
        ],
        "correct_answer": "B",
        "explanation": "LEFT OUTER JOIN preserves all tuples from the left relation, padding unmatched right attributes with NULL."
    },
    {
        "id": 210,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In SQL, what does `EXISTS (SELECT ...)` evaluate to?",
        "options": [
            "(A) True if the subquery returns at least one tuple",
            "(B) Number of rows",
            "(C) True if subquery returns null",
            "(D) False always"
        ],
        "correct_answer": "A",
        "explanation": "`EXISTS` is a boolean operator that evaluates to TRUE if the subquery result is non-empty."
    },
    {
        "id": 211,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "A Superkey of relation R is defined as:",
        "options": [
            "(A) A set of attributes that uniquely identifies every tuple in R",
            "(B) A minimal candidate key",
            "(C) A key with at most one attribute",
            "(D) A foreign key"
        ],
        "correct_answer": "A",
        "explanation": "A superkey is any set of attributes that uniquely determines a tuple. A candidate key is a minimal superkey."
    },
    {
        "id": 212,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "A Candidate Key is:",
        "options": [
            "(A) Any superkey",
            "(B) A minimal superkey (no proper subset is a superkey)",
            "(C) Always numeric",
            "(D) Foreign key"
        ],
        "correct_answer": "B",
        "explanation": "A candidate key is a minimal superkey; removing any attribute destroys the uniqueness property."
    },
    {
        "id": 213,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "A Foreign Key constraint enforces:",
        "options": [
            "(A) Entity integrity",
            "(B) Referential integrity",
            "(C) Domain integrity",
            "(D) User integrity"
        ],
        "correct_answer": "B",
        "explanation": "Referential integrity requires that foreign key values in a referencing table must match existing primary key values in referenced table or be NULL."
    },
    {
        "id": 214,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In relational algebra, the division operator (R \u00f7 S) is used for queries involving:",
        "options": [
            "(A) Ratio calculations",
            "(B) 'For all' / universal quantification conditions",
            "(C) Pattern matching",
            "(D) Aggregation"
        ],
        "correct_answer": "B",
        "explanation": "Division R \u00f7 S finds tuples in R that are associated with ALL tuples in S."
    },
    {
        "id": 215,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What is the output of `SELECT 5 + NULL` in SQL?",
        "options": [
            "(A) 5",
            "(B) 0",
            "(C) NULL",
            "(D) Error"
        ],
        "correct_answer": "C",
        "explanation": "Any arithmetic operation with NULL results in NULL in SQL three-valued logic."
    },
    {
        "id": 216,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In an ER diagram, a multi-valued attribute is represented by:",
        "options": [
            "(A) Rectangle",
            "(B) Double ellipse (oval)",
            "(C) Dashed ellipse",
            "(D) Diamond"
        ],
        "correct_answer": "B",
        "explanation": "Multi-valued attributes (e.g. phone numbers) are represented by double concentric ellipses."
    },
    {
        "id": 217,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In an ER diagram, a derived attribute is represented by:",
        "options": [
            "(A) Dashed ellipse",
            "(B) Double rectangle",
            "(C) Triangle",
            "(D) Hexagon"
        ],
        "correct_answer": "A",
        "explanation": "Derived attributes (e.g. age calculated from date of birth) are drawn as dashed ellipses."
    },
    {
        "id": 218,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "In an ER diagram, relationship sets are represented by:",
        "options": [
            "(A) Rectangles",
            "(B) Diamonds",
            "(C) Ellipses",
            "(D) Lines"
        ],
        "correct_answer": "B",
        "explanation": "Entity sets are rectangles; attributes are ellipses; relationships are diamonds."
    },
    {
        "id": 219,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What does `ON DELETE CASCADE` specify on a foreign key?",
        "options": [
            "(A) Prevents deletion of parent row",
            "(B) Automatically deletes referencing rows when referenced parent row is deleted",
            "(C) Sets child to NULL",
            "(D) Rolls back transaction"
        ],
        "correct_answer": "B",
        "explanation": "`CASCADE` automatically propagates parent deletion to corresponding child tuples."
    },
    {
        "id": 220,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What SQL keyword eliminates duplicate rows from query results?",
        "options": [
            "(A) UNIQUE",
            "(B) DISTINCT",
            "(C) DIFFERENT",
            "(D) CLEAN"
        ],
        "correct_answer": "B",
        "explanation": "`SELECT DISTINCT` eliminates duplicate tuples from output."
    },
    {
        "id": 221,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What does a correlated subquery mean in SQL?",
        "options": [
            "(A) Subquery that runs only once",
            "(B) Subquery that references columns from outer query and executes once per outer row",
            "(C) Parallel query",
            "(D) Recursive query"
        ],
        "correct_answer": "B",
        "explanation": "A correlated subquery references values in the outer query, evaluating once for every candidate row of the outer query."
    },
    {
        "id": 222,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "Which SQL aggregate function computes the total number of non-null values in a column?",
        "options": [
            "(A) SUM()",
            "(B) COUNT(column)",
            "(C) TOTAL()",
            "(D) LENGTH()"
        ],
        "correct_answer": "B",
        "explanation": "`COUNT(column)` counts all non-null values in the specified column."
    },
    {
        "id": 223,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "The primary key of a relation CANNOT contain:",
        "options": [
            "(A) Integers",
            "(B) Strings",
            "(C) NULL values",
            "(D) Foreign keys"
        ],
        "correct_answer": "C",
        "explanation": "Entity integrity constraint strictly mandates that primary key attributes cannot contain NULL."
    },
    {
        "id": 224,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What is the degree of a relation?",
        "options": [
            "(A) Number of tuples (rows)",
            "(B) Number of attributes (columns)",
            "(C) Number of primary keys",
            "(D) Depth of B+ tree"
        ],
        "correct_answer": "B",
        "explanation": "Degree = number of attributes (columns). Cardinality = number of tuples (rows)."
    },
    {
        "id": 225,
        "subject": "Database Management and Warehousing",
        "chapter": "Relational Databases & SQL",
        "question": "What is the cardinality of a relation with 100 rows?",
        "options": [
            "(A) 100",
            "(B) Number of columns",
            "(C) Unknown",
            "(D) 1"
        ],
        "correct_answer": "A",
        "explanation": "Cardinality is the total count of tuples (rows) in a relation: 100."
    },
    {
        "id": 226,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "According to Armstrong's Axioms, if X -> Y and Y -> Z, then X -> Z. This rule is called:",
        "options": [
            "(A) Reflexivity",
            "(B) Augmentation",
            "(C) Transitivity",
            "(D) Decomposition"
        ],
        "correct_answer": "C",
        "explanation": "Transitivity rule: if X determines Y and Y determines Z, then X determines Z."
    },
    {
        "id": 227,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A relation is in First Normal Form (1NF) if and only if:",
        "options": [
            "(A) It has no foreign keys",
            "(B) All attribute values are atomic (no repeating groups/multivalued)",
            "(C) It is in 2NF",
            "(D) It has BCNF"
        ],
        "correct_answer": "B",
        "explanation": "1NF requires domain of each attribute to contain only atomic (indivisible) values."
    },
    {
        "id": 228,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A relation in 1NF is in Second Normal Form (2NF) if:",
        "options": [
            "(A) No non-prime attribute is partially dependent on any candidate key",
            "(B) All attributes are keys",
            "(C) No transitive dependencies",
            "(D) All FDs are trivial"
        ],
        "correct_answer": "A",
        "explanation": "2NF eliminates partial functional dependencies of non-prime attributes on parts of candidate keys."
    },
    {
        "id": 229,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A relation in 2NF is in Third Normal Form (3NF) if for every non-trivial FD X -> Y:",
        "options": [
            "(A) X is a superkey OR Y is a prime attribute",
            "(B) X is a superkey only",
            "(C) Y is superkey",
            "(D) All attributes are numeric"
        ],
        "correct_answer": "A",
        "explanation": "3NF allows X to be a superkey OR Y to be part of a candidate key (prime attribute), eliminating transitive dependencies."
    },
    {
        "id": 230,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A relation is in Boyce-Codd Normal Form (BCNF) if for every non-trivial FD X -> Y:",
        "options": [
            "(A) X is a superkey",
            "(B) Y is a prime attribute",
            "(C) X \u2229 Y = \u2205",
            "(D) X is foreign key"
        ],
        "correct_answer": "A",
        "explanation": "BCNF strictly requires that the determinant X must be a superkey for every non-trivial functional dependency."
    },
    {
        "id": 231,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "Which normal form guarantees losslessness and dependency preservation, but may permit redundancy?",
        "options": [
            "(A) 3NF",
            "(B) BCNF",
            "(C) 4NF",
            "(D) 5NF"
        ],
        "correct_answer": "A",
        "explanation": "3NF synthesis always guarantees lossless join AND dependency preservation. BCNF cannot always preserve all FDs."
    },
    {
        "id": 232,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A decomposition of relation R into R_1 and R_2 is Lossless Join if and only if R_1 \u2229 R_2 determines:",
        "options": [
            "(A) R_1 or R_2 (R_1 \u2229 R_2 -> R_1 or R_1 \u2229 R_2 -> R_2)",
            "(B) Nothing",
            "(C) Both R_1 and R_2 simultaneously",
            "(D) Empty set"
        ],
        "correct_answer": "A",
        "explanation": "Lossless join requires the intersection of the decomposed schemas to form a superkey of at least one schema."
    },
    {
        "id": 233,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "The ACID property guaranteeing that either all operations of a transaction succeed or none take effect is:",
        "options": [
            "(A) Atomicity",
            "(B) Consistency",
            "(C) Isolation",
            "(D) Durability"
        ],
        "correct_answer": "A",
        "explanation": "Atomicity ('all-or-nothing') ensures incomplete transactions are rolled back completely upon failure."
    },
    {
        "id": 234,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "The ACID property that ensures concurrent execution of transactions produces the same state as serial execution is:",
        "options": [
            "(A) Atomicity",
            "(B) Consistency",
            "(C) Isolation",
            "(D) Durability"
        ],
        "correct_answer": "C",
        "explanation": "Isolation guarantees concurrent transactions run independently without interfering with each other."
    },
    {
        "id": 235,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A schedule is Conflict Serialisable if its precedence (conflict) graph:",
        "options": [
            "(A) Has no cycles (is a DAG)",
            "(B) Contains at least one cycle",
            "(C) Is bipartite",
            "(D) Is complete"
        ],
        "correct_answer": "A",
        "explanation": "A schedule is conflict serializable if and only if its precedence graph contains no directed cycles."
    },
    {
        "id": 236,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "Under the Two-Phase Locking (2PL) protocol, a transaction:",
        "options": [
            "(A) Cannot acquire new locks after releasing any lock",
            "(B) Can acquire and release locks anytime",
            "(C) Only locks read items",
            "(D) Avoids deadlocks"
        ],
        "correct_answer": "A",
        "explanation": "2PL consists of a Growing Phase (locks acquired) and Shrinking Phase (locks released). Once a lock is released, no new locks can be acquired."
    },
    {
        "id": 237,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "Does basic 2PL protocol guarantee freedom from deadlocks?",
        "options": [
            "(A) Yes, always",
            "(B) No, deadlocks are still possible",
            "(C) Only in read transactions",
            "(D) Only if strict"
        ],
        "correct_answer": "B",
        "explanation": "Basic 2PL ensures conflict serializability, but transactions can still enter circular wait (deadlock)."
    },
    {
        "id": 238,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "In Strict Two-Phase Locking (Strict 2PL), all exclusive (write) locks are held until:",
        "options": [
            "(A) The transaction commits or aborts",
            "(B) The growing phase ends",
            "(C) Another transaction requests the lock",
            "(D) End of file"
        ],
        "correct_answer": "A",
        "explanation": "Strict 2PL holds exclusive locks until transaction completion, preventing cascading rollbacks."
    },
    {
        "id": 239,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "In B+ Trees, data pointers to actual records are stored in:",
        "options": [
            "(A) Only leaf nodes",
            "(B) Internal nodes only",
            "(C) Both internal and leaf nodes",
            "(D) Root only"
        ],
        "correct_answer": "A",
        "explanation": "B+ Trees store all actual record pointers in leaf nodes (linked sequentially). Internal nodes store only index search keys."
    },
    {
        "id": 240,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "In B-Trees (unlike B+ Trees), search keys and data pointers are stored in:",
        "options": [
            "(A) Only leaf nodes",
            "(B) Both internal and leaf nodes",
            "(C) Root only",
            "(D) External file"
        ],
        "correct_answer": "B",
        "explanation": "B-trees store data pointers in both internal nodes and leaf nodes, whereas B+ trees store all data pointers exclusively in leaves."
    },
    {
        "id": 241,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "Online Analytical Processing (OLAP) systems typically use which schema design?",
        "options": [
            "(A) 3NF normalized schema",
            "(B) Star and Snowflake schemas with Fact and Dimension tables",
            "(C) Flat unstructured text",
            "(D) Key-value only"
        ],
        "correct_answer": "B",
        "explanation": "Data warehouses use dimensional modeling (Star and Snowflake schemas) centered around Fact tables connected to Dimension tables."
    },
    {
        "id": 242,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "In a Data Warehouse, a Fact Table typically contains:",
        "options": [
            "(A) Descriptive textual attributes",
            "(B) Numerical additive measures and foreign keys to dimension tables",
            "(C) User passwords",
            "(D) Transaction logs"
        ],
        "correct_answer": "B",
        "explanation": "Fact tables contain metrics/measures (e.g. sales quantity, revenue) and foreign keys referencing dimension tables."
    },
    {
        "id": 243,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "The OLAP operation that aggregates data by moving up a concept hierarchy (e.g. from day to month) is called:",
        "options": [
            "(A) Drill-down",
            "(B) Roll-up",
            "(C) Slice",
            "(D) Pivot"
        ],
        "correct_answer": "B",
        "explanation": "Roll-up performs aggregation along a dimension hierarchy (increasing granularity, e.g., Day -> Month -> Year)."
    },
    {
        "id": 244,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "The OLAP operation that steps down from higher-level summary to more detailed data is called:",
        "options": [
            "(A) Roll-up",
            "(B) Drill-down",
            "(C) Dice",
            "(D) Pivot"
        ],
        "correct_answer": "B",
        "explanation": "Drill-down navigates from less detailed data to more detailed data (e.g. Year -> Quarter -> Month)."
    },
    {
        "id": 245,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "The OLAP operation that selects a sub-cube by filtering on ONE dimension is called:",
        "options": [
            "(A) Slice",
            "(B) Dice",
            "(C) Pivot",
            "(D) Roll-up"
        ],
        "correct_answer": "A",
        "explanation": "A Slice filters on a single dimension (e.g. time = '2024'). A Dice filters on two or more dimensions."
    },
    {
        "id": 246,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "In a Snowflake Schema, dimension tables are:",
        "options": [
            "(A) Completely denormalized into a single table",
            "(B) Normalized into multiple related tables",
            "(C) Absent",
            "(D) Stored in memory"
        ],
        "correct_answer": "B",
        "explanation": "Snowflake schema normalizes dimension tables to remove redundancy, whereas Star schema keeps dimension tables denormalized."
    },
    {
        "id": 247,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "A clustered index in a relational database:",
        "options": [
            "(A) Dictates the physical storage order of data records in the table",
            "(B) Can be created multiple times per table",
            "(C) Stores only duplicate keys",
            "(D) Is always hash-based"
        ],
        "correct_answer": "A",
        "explanation": "A table can have only ONE clustered index because it determines the physical sorted order of rows on disk."
    },
    {
        "id": 248,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "What is the maximum number of clustered indexes a table can have?",
        "options": [
            "(A) 1",
            "(B) 2",
            "(C) Unlimited",
            "(D) Same as number of columns"
        ],
        "correct_answer": "A",
        "explanation": "Data on disk can only be physically sorted in one order, so only 1 clustered index is possible per table."
    },
    {
        "id": 249,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "In the Wait-Die deadlock prevention scheme based on timestamps (where older transaction has smaller timestamp):",
        "options": [
            "(A) Older waits for younger; younger dies if requesting lock held by older",
            "(B) Younger waits for older",
            "(C) Older always dies",
            "(D) Both transactions die"
        ],
        "correct_answer": "A",
        "explanation": "Wait-Die is non-preemptive: if T_old requests resource held by T_young, T_old waits. If T_young requests resource held by T_old, T_young dies."
    },
    {
        "id": 250,
        "subject": "Database Management and Warehousing",
        "chapter": "Normalization & Data Warehousing",
        "question": "If an FD set F on R(A, B, C) is {A -> B, B -> C}, the candidate key of R is:",
        "options": [
            "(A) B",
            "(B) C",
            "(C) A",
            "(D) BC"
        ],
        "correct_answer": "C",
        "explanation": "Closure of A: A^+ = {A, B, C}. Since A determines all attributes and is minimal, A is the unique candidate key."
    },
    {
        "id": 251,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Ordinary Least Squares (OLS) Linear Regression, the closed-form Normal Equation for weights w is:",
        "options": [
            "(A) w = (X^T X)^{-1} X^T y",
            "(B) w = X^T y",
            "(C) w = (X X^T)^{-1} y",
            "(D) w = X^{-1} y"
        ],
        "correct_answer": "A",
        "explanation": "Setting the gradient of residual sum of squares \u2207_w ||Xw - y||^2 = 2X^T (Xw - y) = 0 yields w = (X^T X)^{-1} X^T y."
    },
    {
        "id": 252,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Ridge Regression, the regularization term added to the loss function is:",
        "options": [
            "(A) \u03bb ||w||_1",
            "(B) \u03bb ||w||_2^2",
            "(C) \u03bb ||w||_0",
            "(D) \u03bb ln(w)"
        ],
        "correct_answer": "B",
        "explanation": "Ridge adds an L2 penalty \u03bb \u2211 w_i^2, shrinking coefficients towards zero."
    },
    {
        "id": 253,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Lasso Regression, the regularization term added to the loss function is:",
        "options": [
            "(A) \u03bb ||w||_2^2",
            "(B) \u03bb ||w||_1 = \u03bb \u2211 |w_i|",
            "(C) \u03bb ||w||_\u221e",
            "(D) \u03bb w^T X w"
        ],
        "correct_answer": "B",
        "explanation": "Lasso adds an L1 penalty \u03bb \u2211 |w_i|, producing sparse weight vectors (exact feature selection)."
    },
    {
        "id": 254,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "High bias in a machine learning model is typically associated with:",
        "options": [
            "(A) Overfitting",
            "(B) Underfitting",
            "(C) High variance",
            "(D) Zero training error"
        ],
        "correct_answer": "B",
        "explanation": "High bias means the model is too simple to capture underlying data patterns, causing underfitting."
    },
    {
        "id": 255,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "High variance in a machine learning model is typically characterized by:",
        "options": [
            "(A) Low training error and high test error (overfitting)",
            "(B) High training error and high test error",
            "(C) Underfitting",
            "(D) High regularization"
        ],
        "correct_answer": "A",
        "explanation": "High variance means the model fits training data noise too closely, failing to generalize to unseen test data."
    },
    {
        "id": 256,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "The logistic (sigmoid) function \u03c3(z) is defined as:",
        "options": [
            "(A) 1 / (1 + e^{-z})",
            "(B) e^z / (1 + e^z)",
            "(C) Both A and B are mathematically identical",
            "(D) (e^z - e^{-z}) / 2"
        ],
        "correct_answer": "C",
        "explanation": "1 / (1 + e^{-z}) = e^z / (e^z + 1). Both expressions represent the sigmoid function mapping R -> (0, 1)."
    },
    {
        "id": 257,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Logistic Regression, the log-odds (logit) ln(p / (1 - p)) is modeled as:",
        "options": [
            "(A) A linear combination of input features w^T x + b",
            "(B) A quadratic function",
            "(C) Exponential",
            "(D) Sigmoid"
        ],
        "correct_answer": "A",
        "explanation": "Logistic regression models the log-odds (logit) linearly: ln(p / (1 - p)) = w^T x + b."
    },
    {
        "id": 258,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "What loss function is minimized in binary Logistic Regression?",
        "options": [
            "(A) Mean Squared Error",
            "(B) Binary Cross-Entropy (Log Loss)",
            "(C) Hinge Loss",
            "(D) Absolute Error"
        ],
        "correct_answer": "B",
        "explanation": "Logistic regression maximizes likelihood, which is equivalent to minimizing Binary Cross-Entropy: -\u2211 [y ln p + (1-y) ln(1-p)]."
    },
    {
        "id": 259,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Support Vector Machines (SVM), the decision boundary maximizes:",
        "options": [
            "(A) The number of training errors",
            "(B) The margin (distance to closest training points)",
            "(C) The number of features",
            "(D) Total variance"
        ],
        "correct_answer": "B",
        "explanation": "SVM is a maximum-margin classifier: it finds the hyperplane that maximizes the geometric distance to nearest data points (support vectors)."
    },
    {
        "id": 260,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "The points in SVM that lie on the margin boundaries and determine the decision hyperplane are called:",
        "options": [
            "(A) Outliers",
            "(B) Support Vectors",
            "(C) Centroids",
            "(D) Kernels"
        ],
        "correct_answer": "B",
        "explanation": "Support vectors are data points that constrain the margin; moving other points does not alter the decision boundary."
    },
    {
        "id": 261,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In soft-margin SVM, the hyperparameter C controls the tradeoff between:",
        "options": [
            "(A) Learning rate and momentum",
            "(B) Margin maximization and slack penalty (margin violation)",
            "(C) Number of trees and depth",
            "(D) Bias and PCA"
        ],
        "correct_answer": "B",
        "explanation": "Large C penalizes margin violations heavily (smaller margin, lower bias). Small C allows more violations (larger margin, lower variance)."
    },
    {
        "id": 262,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "The Kernel Trick in SVM allows learning non-linear decision boundaries by:",
        "options": [
            "(A) Computing dot products in high-dimensional feature space without explicitly mapping vectors",
            "(B) Inverting the kernel matrix",
            "(C) Discarding features",
            "(D) Adding random noise"
        ],
        "correct_answer": "A",
        "explanation": "Mercer's theorem allows computing K(x, z) = \u27e8\u03c6(x), \u03c6(z)\u27e9 directly in input space without explicit coordinate transformation."
    },
    {
        "id": 263,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "The Radial Basis Function (RBF) / Gaussian kernel is defined as:",
        "options": [
            "(A) exp(-\u03b3 ||x - z||^2)",
            "(B) (x^T z + c)^d",
            "(C) tanh(x^T z)",
            "(D) x^T z"
        ],
        "correct_answer": "A",
        "explanation": "The RBF Gaussian kernel is K(x, z) = exp(-\u03b3 ||x - z||^2) = exp(-||x - z||^2 / (2\u03c3^2))."
    },
    {
        "id": 264,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "What splitting criterion in Decision Trees measures impurity using H(S) = -\u2211 p_i log_2 p_i?",
        "options": [
            "(A) Gini Impurity",
            "(B) Entropy",
            "(C) Variance",
            "(D) Misclassification rate"
        ],
        "correct_answer": "B",
        "explanation": "Shannon Entropy measures average information content and impurity: H(S) = -\u2211 p_i log_2 p_i."
    },
    {
        "id": 265,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "The Gini Impurity for a set with class probabilities p_i is defined as:",
        "options": [
            "(A) 1 - \u2211 p_i^2",
            "(B) -\u2211 p_i log p_i",
            "(C) \u220f p_i",
            "(D) max(p_i)"
        ],
        "correct_answer": "A",
        "explanation": "Gini Impurity = 1 - \u2211_{i=1}^C p_i^2 (used in CART trees)."
    },
    {
        "id": 266,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Information Gain from splitting on feature A is defined as:",
        "options": [
            "(A) H(Parent) - H(Children)",
            "(B) H(Parent) + H(Children)",
            "(C) H(Children) / H(Parent)",
            "(D) H(Parent) * H(Children)"
        ],
        "correct_answer": "A",
        "explanation": "Information Gain = Entropy(Parent) - \u2211 (|S_v| / |S|) Entropy(S_v)."
    },
    {
        "id": 267,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Why are Decision Trees prone to high variance (overfitting)?",
        "options": [
            "(A) They are linear models",
            "(B) Fully grown trees can create complex boundaries that isolate every training sample",
            "(C) They cannot handle categorical data",
            "(D) High regularization"
        ],
        "correct_answer": "B",
        "explanation": "Without pruning or depth limits, decision trees can recursively split until every leaf contains a single pure sample."
    },
    {
        "id": 268,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Bagging (Bootstrap Aggregating) primarily reduces:",
        "options": [
            "(A) Bias",
            "(B) Variance",
            "(C) Computation time",
            "(D) Number of features"
        ],
        "correct_answer": "B",
        "explanation": "Averaging multiple independent low-bias, high-variance models (e.g. deep trees) significantly reduces model variance."
    },
    {
        "id": 269,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Random Forests improve upon standard Bagging by:",
        "options": [
            "(A) Subsampling a random subset of features at each split to decorrelate trees",
            "(B) Training trees sequentially",
            "(C) Using boosting",
            "(D) Using only one tree"
        ],
        "correct_answer": "A",
        "explanation": "Random Forests randomly select a feature subset (typically \u221ad) at each candidate split, decorrelating the ensemble trees."
    },
    {
        "id": 270,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Boosting algorithms (such as AdaBoost), individual base learners are trained:",
        "options": [
            "(A) In parallel independently",
            "(B) Sequentially, with higher weights assigned to previously misclassified samples",
            "(C) Without any labels",
            "(D) Using random projections"
        ],
        "correct_answer": "B",
        "explanation": "Boosting trains weak learners sequentially; each successive model focuses on errors made by previous models."
    },
    {
        "id": 271,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Gradient Boosting fits each new tree to the:",
        "options": [
            "(A) Original target labels y",
            "(B) Pseudo-residuals (negative gradient of loss function)",
            "(C) Average of previous trees",
            "(D) Inverse covariance"
        ],
        "correct_answer": "B",
        "explanation": "Gradient Boosting performs gradient descent in function space by fitting new base learners to negative gradients (residuals)."
    },
    {
        "id": 272,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "The loss function used in Support Vector Machines is:",
        "options": [
            "(A) Cross-entropy loss",
            "(B) Hinge loss: max(0, 1 - y * f(x))",
            "(C) Mean squared error",
            "(D) Huber loss"
        ],
        "correct_answer": "B",
        "explanation": "SVM minimizes regularized Hinge loss: L(w) = (1/2)||w||^2 + C \u2211 max(0, 1 - y_i (w^T x_i + b))."
    },
    {
        "id": 273,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "In Linear Regression, if features are collinear (multicollinearity), what issue arises?",
        "options": [
            "(A) Model trains too fast",
            "(B) X^T X is nearly singular (unstable matrix inversion and high variance of coefficients)",
            "(C) Training error becomes zero",
            "(D) Underfitting"
        ],
        "correct_answer": "B",
        "explanation": "Multicollinearity makes X^T X non-invertible or ill-conditioned, causing huge standard errors and volatile coefficients."
    },
    {
        "id": 274,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Pruning a decision tree (e.g. cost-complexity pruning) helps to:",
        "options": [
            "(A) Increase training accuracy",
            "(B) Combat overfitting and improve generalization on test data",
            "(C) Increase tree depth",
            "(D) Convert tree to neural net"
        ],
        "correct_answer": "B",
        "explanation": "Pruning removes subtrees with low predictive power, reducing variance and preventing overfitting."
    },
    {
        "id": 275,
        "subject": "Machine Learning",
        "chapter": "Supervised Learning",
        "question": "Which ensemble method typically uses shallow trees (weak learners) with high bias and low variance?",
        "options": [
            "(A) Random Forest",
            "(B) Bagging",
            "(C) Boosting (e.g. AdaBoost, Gradient Boost)",
            "(D) Deep Decision Trees"
        ],
        "correct_answer": "C",
        "explanation": "Boosting ensembles weak learners (stumps/shallow trees with high bias) sequentially to iteratively reduce bias."
    },
    {
        "id": 276,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In K-Nearest Neighbors (KNN), classification of a query point is based on:",
        "options": [
            "(A) A parametric probability distribution",
            "(B) Majority vote among its k nearest neighbors in feature space",
            "(C) Decision tree splits",
            "(D) Linear hyperplane"
        ],
        "correct_answer": "B",
        "explanation": "KNN is a non-parametric instance-based algorithm assigning class by majority vote among k closest training examples."
    },
    {
        "id": 277,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In KNN, what happens if k = 1?",
        "options": [
            "(A) The model has high bias",
            "(B) The model has high variance (very flexible boundary, sensitive to noise)",
            "(C) The model produces a linear boundary",
            "(D) The model never makes training error"
        ],
        "correct_answer": "B",
        "explanation": "k = 1 fits training data perfectly (zero training error) but has extreme sensitivity to noise (high variance)."
    },
    {
        "id": 278,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In KNN, as k -> \u221e (equal to total training samples N), the model predicts:",
        "options": [
            "(A) Training sample noise",
            "(B) The majority class of the entire training dataset (high bias)",
            "(C) Zero",
            "(D) Random class"
        ],
        "correct_answer": "B",
        "explanation": "Large k smooths decision boundaries, ultimately predicting the global majority class for every query point."
    },
    {
        "id": 279,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "What distance metric is equivalent to L2 norm: d(x, y) = \u221a(\u2211 (x_i - y_i)^2)?",
        "options": [
            "(A) Manhattan distance (L1)",
            "(B) Euclidean distance (L2)",
            "(C) Chebyshev distance (L\u221e)",
            "(D) Cosine distance"
        ],
        "correct_answer": "B",
        "explanation": "Euclidean distance is the square root of the sum of squared differences (L2 norm)."
    },
    {
        "id": 280,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "K-Means clustering minimizes which objective function?",
        "options": [
            "(A) Within-Cluster Sum of Squares (Inertia: \u2211 ||x_i - \u03bc_c||^2)",
            "(B) Between-cluster distance",
            "(C) Maximum margin",
            "(D) Cross-entropy"
        ],
        "correct_answer": "A",
        "explanation": "K-Means minimizes WCSS (inertia): J = \u2211_{k=1}^K \u2211_{x \u2208 C_k} ||x - \u03bc_k||^2."
    },
    {
        "id": 281,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "K-Means++ improves over standard random initialization by:",
        "options": [
            "(A) Selecting initial cluster centers with probability proportional to squared distance from nearest chosen center",
            "(B) Using gradient descent",
            "(C) Always choosing first k samples",
            "(D) Running PCA first"
        ],
        "correct_answer": "A",
        "explanation": "K-Means++ spaces initial centers far apart by sampling with probability proportional to D(x)^2, speeding convergence."
    },
    {
        "id": 282,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "What method helps determine the optimal number of clusters k in K-Means?",
        "options": [
            "(A) Elbow Method (and Silhouette Analysis)",
            "(B) Cross-validation loss",
            "(C) L'Hopital rule",
            "(D) Normal equation"
        ],
        "correct_answer": "A",
        "explanation": "The Elbow method plots WCSS vs k looking for the point of diminishing returns (elbow); Silhouette score measures cohesion vs separation."
    },
    {
        "id": 283,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "The Silhouette coefficient of a sample is bounded within:",
        "options": [
            "(A) [0, 1]",
            "(B) [-1, 1]",
            "(C) (-\u221e, \u221e)",
            "(D) [0, 100]"
        ],
        "correct_answer": "B",
        "explanation": "Silhouette score s = (b - a) / max(a, b) lies in [-1, 1]. Near +1 indicates well-clustered points; negative indicates wrong cluster assignment."
    },
    {
        "id": 284,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "DBSCAN (Density-Based Spatial Clustering) identifies clusters based on:",
        "options": [
            "(A) Centroids and WCSS",
            "(B) Density connectivity (Core points with at least MinPts within radius \u03b5)",
            "(C) Hyperplanes",
            "(D) Gaussian mixture weights"
        ],
        "correct_answer": "B",
        "explanation": "DBSCAN groups points with high local density (\u2265 MinPts in \u03b5-neighborhood) and identifies noise/outliers naturally."
    },
    {
        "id": 285,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Which clustering algorithm can discover arbitrarily shaped (non-spherical) clusters and handle outliers?",
        "options": [
            "(A) K-Means",
            "(B) DBSCAN",
            "(C) Linear Regression",
            "(D) Logistic Regression"
        ],
        "correct_answer": "B",
        "explanation": "DBSCAN does not assume spherical clusters and labels sparse points as noise, unlike K-Means."
    },
    {
        "id": 286,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Principal Component Analysis (PCA) performs dimensionality reduction by:",
        "options": [
            "(A) Projecting data onto directions of maximum variance",
            "(B) Minimizing classification error",
            "(C) Non-linear feature mapping",
            "(D) Random feature selection"
        ],
        "correct_answer": "A",
        "explanation": "PCA finds orthogonal axes (eigenvectors of covariance matrix) that maximize projected data variance."
    },
    {
        "id": 287,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In PCA, the proportion of variance explained by the i-th principal component is:",
        "options": [
            "(A) \u03bb_i / \u2211 \u03bb_j",
            "(B) \u03bb_i^2",
            "(C) \u2211 \u03bb_j / \u03bb_i",
            "(D) 1 / \u03bb_i"
        ],
        "correct_answer": "A",
        "explanation": "Explained variance ratio of component i is its eigenvalue divided by the trace (sum of all eigenvalues)."
    },
    {
        "id": 288,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Before applying PCA, it is essential to:",
        "options": [
            "(A) Binarize the labels",
            "(B) Mean-center (and standardize) the features",
            "(C) Shuffle labels",
            "(D) Cluster the data"
        ],
        "correct_answer": "B",
        "explanation": "PCA requires centering data around the origin (\u03bc = 0) so the covariance matrix accurately captures variance."
    },
    {
        "id": 289,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In a binary classification confusion matrix, Precision is defined as:",
        "options": [
            "(A) TP / (TP + FP)",
            "(B) TP / (TP + FN)",
            "(C) (TP + TN) / Total",
            "(D) TN / (TN + FP)"
        ],
        "correct_answer": "A",
        "explanation": "Precision = TP / (TP + FP) measures the fraction of predicted positive examples that are truly positive."
    },
    {
        "id": 290,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In a binary classification confusion matrix, Recall (Sensitivity) is defined as:",
        "options": [
            "(A) TP / (TP + FP)",
            "(B) TP / (TP + FN)",
            "(C) TN / (TN + FP)",
            "(D) FP / (FP + TN)"
        ],
        "correct_answer": "B",
        "explanation": "Recall = TP / (TP + FN) measures the fraction of actual positive examples correctly identified."
    },
    {
        "id": 291,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "The F1-score is the mathematical:",
        "options": [
            "(A) Arithmetic mean of Precision and Recall",
            "(B) Harmonic mean of Precision and Recall: 2*(P*R)/(P+R)",
            "(C) Geometric mean of Precision and Recall",
            "(D) Sum of Precision and Recall"
        ],
        "correct_answer": "B",
        "explanation": "F1 is the harmonic mean: 2 / (1/P + 1/R) = 2 * (P * R) / (P + R). It balances precision and recall."
    },
    {
        "id": 292,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Specificity (True Negative Rate) is defined as:",
        "options": [
            "(A) TN / (TN + FP)",
            "(B) TP / (TP + FN)",
            "(C) TN / (TN + FN)",
            "(D) FP / (TN + FP)"
        ],
        "correct_answer": "A",
        "explanation": "Specificity = TN / (TN + FP) measures the fraction of actual negatives correctly classified as negative."
    },
    {
        "id": 293,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "The Receiver Operating Characteristic (ROC) curve plots:",
        "options": [
            "(A) True Positive Rate vs False Positive Rate at various thresholds",
            "(B) Precision vs Recall",
            "(C) Training error vs Test error",
            "(D) Loss vs Epochs"
        ],
        "correct_answer": "A",
        "explanation": "ROC curve plots TPR (Recall) on y-axis against FPR (1 - Specificity) on x-axis across classification thresholds."
    },
    {
        "id": 294,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "An ROC curve with Area Under Curve (AUC) = 0.5 indicates:",
        "options": [
            "(A) Perfect classification",
            "(B) Performance no better than random guessing",
            "(C) 100% precision",
            "(D) Zero false alarms"
        ],
        "correct_answer": "B",
        "explanation": "AUC = 0.5 corresponds to the diagonal chance line (random coin toss). AUC = 1.0 represents a perfect classifier."
    },
    {
        "id": 295,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "When evaluating models on an extremely imbalanced dataset (e.g. 99% negative, 1% positive), which metric is LEAST informative?",
        "options": [
            "(A) Precision-Recall curve",
            "(B) Overall Accuracy",
            "(C) F1-score",
            "(D) AUC-ROC"
        ],
        "correct_answer": "B",
        "explanation": "A naive model predicting 'Negative' always achieves 99% accuracy on 99:1 imbalanced data while learning nothing."
    },
    {
        "id": 296,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In k-Fold Cross-Validation, the dataset is partitioned into k folds, and the model is trained:",
        "options": [
            "(A) Once on all data",
            "(B) k times, each time using k-1 folds for training and 1 fold for validation",
            "(C) k times on test data",
            "(D) Using only 1 fold"
        ],
        "correct_answer": "B",
        "explanation": "k-fold CV trains k separate models, averaging validation metrics to produce a robust performance estimate."
    },
    {
        "id": 297,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Stratified k-Fold Cross-Validation ensures that:",
        "options": [
            "(A) Each fold contains approximately the same percentage of each target class as the complete dataset",
            "(B) Folds are created sorted by feature",
            "(C) Test data is used for training",
            "(D) k equals sample size"
        ],
        "correct_answer": "A",
        "explanation": "Stratification preserves class proportions across all folds, critical for imbalanced classification tasks."
    },
    {
        "id": 298,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Leave-One-Out Cross-Validation (LOOCV) is a special case of k-fold CV where:",
        "options": [
            "(A) k = 1",
            "(B) k = N (number of data samples)",
            "(C) k = 10",
            "(D) k = 2"
        ],
        "correct_answer": "B",
        "explanation": "LOOCV sets k = N: each model trains on N - 1 samples and evaluates on the single remaining sample."
    },
    {
        "id": 299,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "Hierarchical Agglomerative Clustering uses a 'bottom-up' approach where:",
        "options": [
            "(A) All points start in one cluster and are divided",
            "(B) Each point starts as its own cluster and closest pairs are iteratively merged",
            "(C) Centroids are updated via gradient descent",
            "(D) Data is projected onto 1D"
        ],
        "correct_answer": "B",
        "explanation": "Agglomerative clustering starts with N clusters and successively merges nearest clusters until 1 root remains."
    },
    {
        "id": 300,
        "subject": "Machine Learning",
        "chapter": "Unsupervised Learning & Evaluation",
        "question": "In Hierarchical clustering, 'Complete Linkage' calculates cluster distance as:",
        "options": [
            "(A) Distance between nearest pair of points in the clusters",
            "(B) Maximum distance between any point in cluster A and any point in cluster B",
            "(C) Distance between centroids",
            "(D) Average of all pairs"
        ],
        "correct_answer": "B",
        "explanation": "Complete linkage uses maximum pairwise distance: d(A, B) = max { d(x, y) : x \u2208 A, y \u2208 B }."
    },
    {
        "id": 301,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In AI agent design, what does the acronym PEAS stand for?",
        "options": [
            "(A) Process, Entity, Action, State",
            "(B) Performance measure, Environment, Actuators, Sensors",
            "(C) Perception, Environment, Algorithm, Search",
            "(D) Planning, Evaluation, Action, Solution"
        ],
        "correct_answer": "B",
        "explanation": "PEAS stands for Performance measure, Environment, Actuators, Sensors."
    },
    {
        "id": 302,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "An environment is called 'Deterministic' if:",
        "options": [
            "(A) The next state of the environment is completely determined by the current state and the agent's action",
            "(B) The environment changes while agent is deliberating",
            "(C) Multiple agents are present",
            "(D) State cannot be observed"
        ],
        "correct_answer": "A",
        "explanation": "Deterministic environments exhibit no randomness; current state and action uniquely fix the outcome."
    },
    {
        "id": 303,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Breadth-First Search (BFS) is guaranteed to find the shallowest goal node (optimal for unit edge costs), with space complexity:",
        "options": [
            "(A) O(b*d)",
            "(B) O(b^d)",
            "(C) O(d)",
            "(D) O(1)"
        ],
        "correct_answer": "B",
        "explanation": "BFS stores all explored nodes level by level, leading to exponential memory consumption O(b^d)."
    },
    {
        "id": 304,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Depth-First Search (DFS) has space complexity (where b is branching factor and m is maximum depth):",
        "options": [
            "(A) O(b * m)",
            "(B) O(b^m)",
            "(C) O(m^b)",
            "(D) O(1)"
        ],
        "correct_answer": "A",
        "explanation": "DFS only needs to store the current path from root to leaf, giving linear space complexity O(b * m)."
    },
    {
        "id": 305,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Iterative Deepening Search (IDS) combines:",
        "options": [
            "(A) BFS's completeness and optimality with DFS's O(b*d) linear space complexity",
            "(B) Greedy search with A*",
            "(C) Heuristics with random walks",
            "(D) Minimax with Alpha-Beta"
        ],
        "correct_answer": "A",
        "explanation": "IDS runs depth-limited searches with increasing limits, achieving optimality and completeness with linear space."
    },
    {
        "id": 306,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Uniform Cost Search (UCS) expands the node n with the lowest:",
        "options": [
            "(A) Heuristic estimate h(n)",
            "(B) Path cost g(n) from the start node",
            "(C) Total f(n) = g(n) + h(n)",
            "(D) Depth"
        ],
        "correct_answer": "B",
        "explanation": "UCS orders the priority queue strictly by path cost g(n), guaranteeing optimality for positive step costs."
    },
    {
        "id": 307,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Greedy Best-First Search evaluates nodes using:",
        "options": [
            "(A) f(n) = g(n)",
            "(B) f(n) = h(n)",
            "(C) f(n) = g(n) + h(n)",
            "(D) f(n) = g(n) - h(n)"
        ],
        "correct_answer": "B",
        "explanation": "Greedy Best-First search expands the node that appears closest to the goal according to heuristic h(n)."
    },
    {
        "id": 308,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In A* search, the evaluation function is:",
        "options": [
            "(A) f(n) = g(n) - h(n)",
            "(B) f(n) = g(n) + h(n)",
            "(C) f(n) = g(n) * h(n)",
            "(D) f(n) = max(g, h)"
        ],
        "correct_answer": "B",
        "explanation": "A* balances cost to reach node g(n) with estimated cost to goal h(n): f(n) = g(n) + h(n)."
    },
    {
        "id": 309,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "A heuristic h(n) is called Admissible if for all nodes n:",
        "options": [
            "(A) h(n) \u2265 h*(n)",
            "(B) h(n) \u2264 h*(n) (never overestimates the true cost to goal)",
            "(C) h(n) = 0",
            "(D) h(n) is negative"
        ],
        "correct_answer": "B",
        "explanation": "Admissibility requires h(n) to never overestimate the true remaining cost h*(n) to the nearest goal."
    },
    {
        "id": 310,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "For Tree-Search A*, what condition on heuristic h(n) guarantees an optimal solution?",
        "options": [
            "(A) Consistency (monotonicity)",
            "(B) Admissibility",
            "(C) Strict positivity",
            "(D) Linear linearity"
        ],
        "correct_answer": "B",
        "explanation": "Admissibility is sufficient for A* Tree Search optimality. Consistency is required for Graph Search without reopening closed nodes."
    },
    {
        "id": 311,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "A heuristic is Consistent (Monotone) if for every node n and successor n' generated by action a with step cost c(n, a, n'):",
        "options": [
            "(A) h(n) \u2264 c(n, a, n') + h(n')",
            "(B) h(n) \u2265 c(n, a, n') + h(n')",
            "(C) h(n) = h(n')",
            "(D) h(n) > 0"
        ],
        "correct_answer": "A",
        "explanation": "Consistency satisfies triangle inequality: h(n) \u2264 c(n, a, n') + h(n'). Every consistent heuristic is admissible."
    },
    {
        "id": 312,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "If heuristic h_2(n) \u2265 h_1(n) for all nodes n, and both are admissible, we say:",
        "options": [
            "(A) h_1 dominates h_2",
            "(B) h_2 dominates h_1 (and h_2 expands fewer or equal nodes than h_1 in A*)",
            "(C) h_2 is inconsistent",
            "(D) Both are identical"
        ],
        "correct_answer": "B",
        "explanation": "h_2 dominates h_1: tighter bounds lead to fewer node expansions in A* search."
    },
    {
        "id": 313,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Simulated Annealing avoids getting trapped in local maxima by:",
        "options": [
            "(A) Never accepting bad moves",
            "(B) Accepting worse moves with probability P = exp(\u0394E / T) where temperature T cools over time",
            "(C) Resetting the search randomly",
            "(D) Increasing heuristic weights"
        ],
        "correct_answer": "B",
        "explanation": "The Metropolis criterion accepts inferior moves with probability exp(\u0394E / T), which decreases as T drops."
    },
    {
        "id": 314,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In adversarial search (game theory), the Minimax algorithm assumes that:",
        "options": [
            "(A) The opponent plays randomly",
            "(B) The opponent plays optimally to minimize our utility",
            "(C) Both players cooperate",
            "(D) Payoffs are non-zero sum"
        ],
        "correct_answer": "B",
        "explanation": "Minimax assumes an optimal adversary in two-player zero-sum perfect information games."
    },
    {
        "id": 315,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Alpha-Beta Pruning optimizes Minimax search by:",
        "options": [
            "(A) Pruning branches that cannot influence the final decision without altering the optimal result",
            "(B) Estimating moves with heuristics",
            "(C) Converting game to single player",
            "(D) Searching only to depth 1"
        ],
        "correct_answer": "A",
        "explanation": "Alpha-Beta pruning yields the exact same minimax decision as full minimax while pruning irrelevant subtrees."
    },
    {
        "id": 316,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In Alpha-Beta pruning, a cutoff occurs whenever:",
        "options": [
            "(A) \u03b1 < \u03b2",
            "(B) \u03b1 \u2265 \u03b2",
            "(C) \u03b1 = 0",
            "(D) \u03b2 = 0"
        ],
        "correct_answer": "B",
        "explanation": "When \u03b1 \u2265 \u03b2, the current branch is worse than a known alternative for one of the players, triggering a prune."
    },
    {
        "id": 317,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In Constraint Satisfaction Problems (CSP), the AC-3 algorithm enforces:",
        "options": [
            "(A) Path consistency",
            "(B) Arc consistency (every value in domain of X_i has an allowed value in domain of X_j)",
            "(C) Global consistency",
            "(D) Node consistency only"
        ],
        "correct_answer": "B",
        "explanation": "AC-3 eliminates values from variable domains that violate binary constraints with neighboring variables."
    },
    {
        "id": 318,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In CSP backtracking search, Forward Checking:",
        "options": [
            "(A) Keeps track of remaining valid values for unassigned variables and terminates branch if any domain becomes empty",
            "(B) Performs full BFS",
            "(C) Solves equations linearly",
            "(D) Assigns all variables at once"
        ],
        "correct_answer": "A",
        "explanation": "Forward checking detects future failures early by updating domains of unassigned variables connected by constraints."
    },
    {
        "id": 319,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "The Minimum Remaining Values (MRV) heuristic in CSP chooses the variable with:",
        "options": [
            "(A) Most constraints on remaining variables",
            "(B) Fewest legal values left in its domain (most constrained variable)",
            "(C) Largest domain",
            "(D) Alphabetical first"
        ],
        "correct_answer": "B",
        "explanation": "MRV ('fail-first' heuristic) picks the variable most likely to cause an early failure to prune dead search branches."
    },
    {
        "id": 320,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In CSP, the Least Constraining Value heuristic chooses the value that:",
        "options": [
            "(A) Rules out the fewest values in the remaining variables",
            "(B) Rules out maximum values",
            "(C) Minimizes variable domain",
            "(D) Is numerically smallest"
        ],
        "correct_answer": "A",
        "explanation": "Least constraining value leaves maximum flexibility for subsequent variable assignments."
    },
    {
        "id": 321,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Hill Climbing search algorithm is prone to which limitation?",
        "options": [
            "(A) High memory usage",
            "(B) Getting stuck on local maxima, ridges, and plateaus",
            "(C) Inability to compute steps",
            "(D) Infinite recursion"
        ],
        "correct_answer": "B",
        "explanation": "Greedy local search cannot look beyond immediate neighbors, getting stuck on local optima or flat shoulders."
    },
    {
        "id": 322,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "In genetic algorithms, the process of combining two parent chromosomes to create offspring is called:",
        "options": [
            "(A) Mutation",
            "(B) Crossover (recombination)",
            "(C) Fitness evaluation",
            "(D) Selection"
        ],
        "correct_answer": "B",
        "explanation": "Crossover exchanges segments between two parent solution strings to generate candidate offspring."
    },
    {
        "id": 323,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "If a game tree has branching factor b and search depth d, full Minimax evaluates how many leaf nodes?",
        "options": [
            "(A) O(b * d)",
            "(B) O(b^d)",
            "(C) O(d^b)",
            "(D) O(b + d)"
        ],
        "correct_answer": "B",
        "explanation": "Full minimax explores the complete game tree of depth d, evaluating b^d leaf positions."
    },
    {
        "id": 324,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "With optimal move ordering, Alpha-Beta pruning reduces the effective branching factor to:",
        "options": [
            "(A) O(b)",
            "(B) O(b^{d/2})",
            "(C) O(d)",
            "(D) O(1)"
        ],
        "correct_answer": "B",
        "explanation": "Perfect move ordering examines b^{d/2} leaves, effectively doubling the search depth reachable within the same time limit."
    },
    {
        "id": 325,
        "subject": "Artificial Intelligence",
        "chapter": "Search Strategies & Logic",
        "question": "Which search algorithm is optimal when step costs are equal?",
        "options": [
            "(A) Depth-First Search",
            "(B) Breadth-First Search",
            "(C) Depth-Limited Search",
            "(D) Random Search"
        ],
        "correct_answer": "B",
        "explanation": "BFS finds the shallowest goal node, which is strictly optimal when all edge costs are identical."
    },
    {
        "id": 326,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In Propositional Logic, a formula is a Tautology (valid) if:",
        "options": [
            "(A) It is true in at least one model",
            "(B) It is true in ALL possible models (interpretations)",
            "(C) It is false in all models",
            "(D) It contains no negations"
        ],
        "correct_answer": "B",
        "explanation": "A sentence is valid (tautology) if and only if it evaluates to TRUE under all possible truth assignments."
    },
    {
        "id": 327,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "A propositional formula is Satisfiable if:",
        "options": [
            "(A) It is true in all models",
            "(B) It is true in AT LEAST ONE model",
            "(C) It is false in all models",
            "(D) It has no variables"
        ],
        "correct_answer": "B",
        "explanation": "Satisfiability requires the existence of at least one assignment of truth values that makes the formula true."
    },
    {
        "id": 328,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "Modus Ponens inference rule states that from \u03b1 and (\u03b1 => \u03b2), one can infer:",
        "options": [
            "(A) \u00ac\u03b1",
            "(B) \u03b2",
            "(C) \u00ac\u03b2",
            "(D) \u03b1 \u2227 \u03b2"
        ],
        "correct_answer": "B",
        "explanation": "Modus Ponens: if premise \u03b1 holds and implication \u03b1 => \u03b2 holds, conclusion \u03b2 necessarily follows."
    },
    {
        "id": 329,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In resolution refutation theorem proving, to prove knowledge base KB \u22a8 \u03b1, we show that:",
        "options": [
            "(A) KB \u2227 \u03b1 is valid",
            "(B) KB \u2227 \u00ac\u03b1 is unsatisfiable (derives empty clause / contradiction)",
            "(C) KB \u2227 \u00ac\u03b1 is satisfiable",
            "(D) KB => \u03b1 is false"
        ],
        "correct_answer": "B",
        "explanation": "Proof by refutation adds negated goal \u00ac\u03b1 to KB and applies resolution to derive a contradiction (empty clause \u25a1)."
    },
    {
        "id": 330,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "A clause in Conjunctive Normal Form (CNF) is:",
        "options": [
            "(A) A conjunction of disjunctions of literals",
            "(B) A disjunction of conjunctions",
            "(C) An implication",
            "(D) Single variable"
        ],
        "correct_answer": "A",
        "explanation": "CNF is a logical AND of clauses, where each clause is a logical OR of literals: (A \u2228 \u00acB) \u2227 (C \u2228 D)."
    },
    {
        "id": 331,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In First-Order Logic, what does the Unification algorithm compute?",
        "options": [
            "(A) Truth tables",
            "(B) Most General Unifier (MGU) substitution \u03b8 that makes two predicates identical",
            "(C) Quantifier removal",
            "(D) CNF clauses"
        ],
        "correct_answer": "B",
        "explanation": "Unification finds a variable substitution \u03b8 such that Subst(\u03b8, p) = Subst(\u03b8, q)."
    },
    {
        "id": 332,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In a Bayesian Network with variables X_1, ..., X_n, the joint probability distribution factors as:",
        "options": [
            "(A) \u220f P(X_i)",
            "(B) \u220f_{i=1}^n P(X_i | Parents(X_i))",
            "(C) \u2211 P(X_i | X_{i-1})",
            "(D) \u220f P(X_i | X_1, ..., X_{i-1})"
        ],
        "correct_answer": "B",
        "explanation": "Bayesian network factorization chain rule: P(X_1, ..., X_n) = \u220f_{i=1}^n P(X_i | Parents(X_i))."
    },
    {
        "id": 333,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In a Bayesian Network, a node X is conditionally independent of all other nodes given its:",
        "options": [
            "(A) Children only",
            "(B) Markov Blanket (Parents, Children, and Children's other parents)",
            "(C) Parents only",
            "(D) Siblings"
        ],
        "correct_answer": "B",
        "explanation": "A node's Markov Blanket (parents, children, and spouses/co-parents) shields it from the rest of the network."
    },
    {
        "id": 334,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In d-separation, in a linear chain structure X -> Y -> Z, are X and Z conditionally independent given Y?",
        "options": [
            "(A) Yes, X \u22a5 Z | Y",
            "(B) No, Y blocks nothing",
            "(C) Only if X is boolean",
            "(D) Never"
        ],
        "correct_answer": "A",
        "explanation": "In a causal/linear chain X -> Y -> Z, conditioning on intermediate node Y blocks the path (d-separates X and Z)."
    },
    {
        "id": 335,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In d-separation, in a common cause (fork) structure X <- Y -> Z, conditioning on Y:",
        "options": [
            "(A) Makes X and Z independent (blocks path)",
            "(B) Connects X and Z",
            "(C) Inverts probabilities",
            "(D) Causes cycle"
        ],
        "correct_answer": "A",
        "explanation": "Conditioning on common cause Y renders the two effects X and Z conditionally independent."
    },
    {
        "id": 336,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In d-separation, in a collider (common effect) structure X -> Y <- Z with unconditioned Y (and no descendants of Y observed):",
        "options": [
            "(A) The path between X and Z is blocked (X and Z are marginally independent)",
            "(B) X and Z are dependent",
            "(C) Path is active",
            "(D) Y is parent"
        ],
        "correct_answer": "A",
        "explanation": "An unobserved collider blocks the path. (Conditioning on a collider or its descendants activates the path - 'explaining away')."
    },
    {
        "id": 337,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In a Hidden Markov Model (HMM), the Markov assumption on hidden states states that:",
        "options": [
            "(A) Current state S_t depends ONLY on previous state S_{t-1}",
            "(B) State depends on all past observations",
            "(C) Observations are independent of states",
            "(D) States never change"
        ],
        "correct_answer": "A",
        "explanation": "First-order Markov property: P(S_t | S_1, ..., S_{t-1}) = P(S_t | S_{t-1})."
    },
    {
        "id": 338,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In HMMs, the Forward algorithm efficiently computes:",
        "options": [
            "(A) Most likely sequence of hidden states",
            "(B) The probability of an observed sequence P(O_1, ..., O_T | \u03bb) (filtering)",
            "(C) Model parameters",
            "(D) Viterbi path"
        ],
        "correct_answer": "B",
        "explanation": "The Forward algorithm uses dynamic programming to calculate observation likelihood P(O | \u03bb) in O(N^2 T) time."
    },
    {
        "id": 339,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In HMMs, the Viterbi algorithm computes:",
        "options": [
            "(A) Total probability of observations",
            "(B) The most probable sequence of hidden states (decoding)",
            "(C) Gradient descent updates",
            "(D) Expectation maximization"
        ],
        "correct_answer": "B",
        "explanation": "The Viterbi dynamic programming algorithm finds the maximum a posteriori path of hidden states argmax_S P(S | O)."
    },
    {
        "id": 340,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In HMMs, the Baum-Welch algorithm is an instance of which general framework used for parameter learning?",
        "options": [
            "(A) Expectation-Maximization (EM)",
            "(B) Q-learning",
            "(C) Backtracking",
            "(D) A* search"
        ],
        "correct_answer": "A",
        "explanation": "Baum-Welch is the EM algorithm for unsupervised estimation of transition and emission matrices in HMMs."
    },
    {
        "id": 341,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "A Markov Decision Process (MDP) is formalized by the tuple:",
        "options": [
            "(A) (S, A, P, R, \u03b3)",
            "(B) (P, E, A, S)",
            "(C) (V, E, W)",
            "(D) (X, D, C)"
        ],
        "correct_answer": "A",
        "explanation": "An MDP consists of States S, Actions A, Transition probabilities P, Reward function R, and Discount factor \u03b3 \u2208 [0, 1)."
    },
    {
        "id": 342,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In an MDP, the discount factor \u03b3 (where 0 \u2264 \u03b3 < 1) ensures:",
        "options": [
            "(A) Rewards in immediate future are valued more than distant future, and infinite horizon values converge",
            "(B) Agent never terminates",
            "(C) State space is discrete",
            "(D) Rewards are always positive"
        ],
        "correct_answer": "A",
        "explanation": "Discounting guarantees mathematical convergence of infinite horizon cumulative return \u2211_{t=0}^\u221e \u03b3^t R_t."
    },
    {
        "id": 343,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "The Bellman Optimality Equation for state value function V*(s) is:",
        "options": [
            "(A) V*(s) = max_a [ R(s, a) + \u03b3 \u2211_{s'} P(s' | s, a) V*(s') ]",
            "(B) V*(s) = R(s) + V*(s)",
            "(C) V*(s) = \u2211_a R(s, a)",
            "(D) V*(s) = \u03b3 V*(s)"
        ],
        "correct_answer": "A",
        "explanation": "Bellman optimality establishes recursive relation: optimal value equals maximum expected immediate reward plus discounted continuation value."
    },
    {
        "id": 344,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "Value Iteration in MDP converges to the unique optimal value function because the Bellman operator is a:",
        "options": [
            "(A) Contraction mapping (Banach fixed point theorem)",
            "(B) Linear operator",
            "(C) Random projection",
            "(D) Symmetric matrix"
        ],
        "correct_answer": "A",
        "explanation": "The Bellman backup operator is a \u03b3-contraction in infinity norm, guaranteeing geometric convergence to a unique fixed point."
    },
    {
        "id": 345,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "Policy Iteration alternates between which two steps?",
        "options": [
            "(A) Policy Evaluation and Policy Improvement",
            "(B) Value iteration and Q-learning",
            "(C) Forward checking and backtracking",
            "(D) Selection and mutation"
        ],
        "correct_answer": "A",
        "explanation": "Policy Iteration evaluates the current policy's value function V^\u03c0, then greedily updates the policy \u03c0'(s) = argmax_a Q^\u03c0(s, a)."
    },
    {
        "id": 346,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In Reinforcement Learning, Q-Learning is classified as an:",
        "options": [
            "(A) Off-policy Temporal Difference algorithm",
            "(B) On-policy Monte Carlo algorithm",
            "(C) Model-based dynamic program",
            "(D) Unsupervised clustering"
        ],
        "correct_answer": "A",
        "explanation": "Q-learning updates Q(s, a) using max_{a'} Q(s', a') regardless of which action was actually taken by the exploration policy (off-policy)."
    },
    {
        "id": 347,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "The Q-Learning update rule is:",
        "options": [
            "(A) Q(s, a) <- Q(s, a) + \u03b1 [ R + \u03b3 max_{a'} Q(s', a') - Q(s, a) ]",
            "(B) Q(s, a) <- R + \u03b3 Q(s, a)",
            "(C) Q(s, a) <- max Q(s', a')",
            "(D) Q(s, a) <- \u03b1 Q(s, a)"
        ],
        "correct_answer": "A",
        "explanation": "Q-learning updates Q towards the TD target R + \u03b3 max_{a'} Q(s', a') with learning rate \u03b1."
    },
    {
        "id": 348,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In Reinforcement Learning, the exploration vs exploitation dilemma is commonly addressed by:",
        "options": [
            "(A) \u03b5-greedy action selection",
            "(B) Always picking the greedy action",
            "(C) Pure random action",
            "(D) Value iteration"
        ],
        "correct_answer": "A",
        "explanation": "\u03b5-greedy selects random actions with probability \u03b5 (exploration) and the best-known greedy action with probability 1 - \u03b5 (exploitation)."
    },
    {
        "id": 349,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "In a Bayes Net with 5 binary variables where no conditional independencies exist (fully connected DAG), how many parameters are needed?",
        "options": [
            "(A) 5",
            "(B) 31 (2^5 - 1)",
            "(C) 10",
            "(D) 25"
        ],
        "correct_answer": "B",
        "explanation": "A general joint distribution over 5 binary variables requires 2^5 - 1 = 31 independent parameters."
    },
    {
        "id": 350,
        "subject": "Artificial Intelligence",
        "chapter": "Reasoning Under Uncertainty",
        "question": "Variable Elimination is an algorithm used in Bayesian Networks for:",
        "options": [
            "(A) Exact probabilistic inference",
            "(B) State space clustering",
            "(C) Logic resolution",
            "(D) Neural network training"
        ],
        "correct_answer": "A",
        "explanation": "Variable elimination computes marginal posterior distributions by summing out irrelevant variables sequentially using factor operations."
    }
]

def get_practice_questions_by_subject(subject: str):
    return [q for q in PRACTICE_QUESTIONS if q['subject'] == subject]

def get_practice_questions_by_chapter(subject: str, chapter: str):
    return [q for q in PRACTICE_QUESTIONS if q['subject'] == subject and q['chapter'] == chapter]
