# Week 6 Lab: Integrate Methods and Explore Learning-Based Extensions

## Objectives

Week 6 is for moving from separate experiments toward a more coherent project direction.

Some teams may still be completing the Week 5 checkpoint. That is fine. If your previous work is not stable yet, your priority should still be making the baseline, experiments, and report reproducible.

For teams that have already completed most Week 5 tasks, this week asks you to push one step further:

- connect different methods you have tried before;
- design a more unified workflow instead of isolated experiments;
- consider whether learning-based ideas such as RL or DL can help;
- evaluate your proposed method on many instances instead of only a few examples;
- prepare clearer evidence for your final project direction.

The goal is not to build a perfect new algorithm immediately. The goal is to define a reasonable next experiment and explain why it may improve the project.

## Who Should Do Which Task

Choose the path that matches your current progress.

### Track A: Finish and Stabilize Previous Work

Choose this track if your Week 5 checkpoint is still incomplete.

Your main tasks are:

- make sure at least one baseline method can run from start to finish;
- verify that the output solution is feasible or clearly explain where it fails;
- clean your result table and experiment logs;
- update your checkpoint note with current progress;
- identify one concrete issue to fix next.

For this track, you do not need to implement a new learning model yet. A stable, well-explained baseline is still the most important foundation.

### Track B: Combine Existing Methods Into One Workflow

Choose this track if you already have more than one method, operator, or experimental idea.

Try to combine them into a more unified method. For example:

- use one method to generate an initial solution, then use another method to improve it;
- use a repair operator after a heuristic produces infeasible routes;
- use local search after a constructive algorithm;
- choose different methods for different instance types;
- combine results from multiple heuristics and keep the best feasible solution.

Your combined workflow should be simple enough to explain clearly.

A useful structure is:

```text
input instance
  -> initial solution method
  -> feasibility check
  -> repair or improvement step
  -> final solution
  -> evaluation table
```

When writing about the workflow, explain:

- what each component does;
- why the components are connected in this order;
- what baseline it should be compared with;
- whether the combined method improves feasibility, objective value, runtime, or robustness.

### Track C: Try an RL-Based Extension

Choose this track only if you already have runnable methods and enough experimental outputs to support the attempt.

One possible idea is to treat different methods or operators as actions.

Before implementing an RL algorithm, first write a complete MDP formulation.

Your MDP description should include:

- state: current instance features, current solution quality, remaining violations, or iteration number;
- action: choose a heuristic, repair operator, local search operator, or parameter setting;
- transition: how the solution or environment changes after an action is applied;
- reward: improvement in objective value, reduction in infeasibility, or faster convergence;
- episode: one complete solving process for an instance;
- terminal condition: when the episode stops, such as reaching a time limit, iteration limit, or no further improvement.

Also explain why this is a reasonable MDP:

- What information must be included in the state?
- Why are the actions meaningful choices?
- Does the reward really reflect the optimization goal?
- Can the environment be simulated using your current code?

This does not need to be a full advanced RL system. A small prototype is acceptable, such as:

- rule-based action selection first, then discuss how RL could replace the rule;
- a simple bandit-style method for choosing operators;
- logging which action works better under which instance condition;
- comparing fixed operator order versus adaptive operator selection.

The key is to make the problem formulation clear.

### Track D: Try a DL-Based Extension

Another possible direction is to use a neural network to learn from existing methods or results.

For example, you may try:

- train a model to predict which method will work better for an instance;
- predict solution quality or runtime from instance features;
- imitate decisions from a heuristic or expert solution;
- learn a score for selecting customers, routes, swaps, or repair moves;
- use generated data from your existing algorithms as training labels.

Before implementing a network, first explain the network design.

Your DL design should include:

- what the input features are;
- the input tensor or data format;
- the network structure, such as MLP, CNN, GNN, Transformer, encoder-decoder, or another architecture;
- what each major module or layer is intended to capture;
- the output of the network;
- what the target label is;
- the loss function;
- where the training data comes from;
- how you will evaluate whether the model is useful.

For routing problems, do not only write "we use a neural network." Explain why the chosen architecture matches the structure of the problem. For example, if the input is a set or graph of customers, explain how the network handles node features, edge distances, depot information, energy constraints, time windows, or route context.

If there is not enough data yet, you can still write a design note and generate a small dataset from your current algorithms.

## Main Task: Write a Week 6 Integration Note

Each team should upload a short Markdown note describing what they did this week.

The note should include the following sections.

### 1. Current Stage

State which track you chose:

- Track A: finish and stabilize previous work;
- Track B: combine existing methods;
- Track C: RL-based extension;
- Track D: DL-based extension.

Briefly explain why this track fits your current progress.

### 2. Method Design

Describe the method or workflow you are working on.

If you are combining methods, include a simple pipeline.

If you are trying RL or DL, include:

- for RL: state, action, transition, reward, episode, and terminal condition;
- for DL: input format, network architecture, output, label, and loss function;
- data source;
- evaluation metric.

### 3. Experiment Plan

Write down at least one concrete experiment.

A good experiment plan should answer:

- What baseline will you compare against?
- Which instances will you test?
- Which metrics will you record?
- What result would count as improvement?
- What failure case do you expect?

Your proposed method should be tested on a reasonably large set of instances.

Running only two or three instances is usually not enough to support a new method. Try to include different instance sizes, distributions, or constraint settings. If your algorithm is slow, you may use smaller instances, but you should still run enough cases to show whether the method is stable.

A suggested minimum is:

- at least 10 instances for a basic method comparison;
- at least 3 different scales or parameter settings if possible;
- multiple random seeds for stochastic methods;
- a summary table that reports average performance, not only the best single case.

If you cannot run many instances, explain the reason clearly, such as runtime limit, unstable implementation, missing data, or infeasible outputs.

Example metrics:

- objective value;
- runtime;
- feasibility rate;
- number of constraint violations;
- improvement over initial solution;
- stability across random seeds.

### 4. Preliminary Result or Implementation Progress

Include at least one piece of evidence, such as:

- a result table;
- a workflow diagram;
- pseudo-code;
- training data format;
- a log excerpt;
- a short explanation of a failed attempt.

It is acceptable if the result is preliminary. The important part is that the progress is concrete and inspectable.

## Suggested Deliverables

### Minimum

- update the project checkpoint from Week 5 or write a Week 6 integration note;
- clearly state which track your team is following;
- include one concrete method design or experiment plan;
- run your proposed method on a batch of instances, or explain clearly why this is not possible yet;
- upload code, pseudo-code, logs, or tables showing current progress.

### Recommended for Teams Ahead of Schedule

- implement a combined workflow using at least two existing methods or operators;
- compare the combined workflow with a simpler baseline on many instances;
- try a small adaptive operator-selection experiment;
- prepare a small dataset for DL/RL experiments;
- report average result, best result, feasibility rate, and runtime across the tested instances;
- write down why the learning-based idea is useful or not useful for your current problem.

## Important Reminder

Learning-based methods are optional and should serve the project, not replace clear thinking.

A method tested on only one or two easy examples is not convincing yet. Even if the proposed idea looks promising, you need enough instances to show whether it works consistently, when it fails, and whether the improvement is meaningful.

Before trying RL or DL, ask:

- Do we have enough data or repeated experiments?
- Is there a clear decision to learn?
- Can we compare the learned method with a simple rule?
- Will this help solve feasibility, objective value, runtime, or robustness?

If the answer is unclear, start with a simpler combined heuristic workflow first.

By the end of Week 6, each team should have a clearer project direction: either a stable baseline ready for final experiments, a combined method worth testing, or a learning-based extension with a concrete formulation.
