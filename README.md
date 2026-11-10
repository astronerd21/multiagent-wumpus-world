# multiagent-wumpus-world

Project for "Intelligente Softwareagenten" @ University of Rostock (WS 2026/27). Multiagent Wumpus World simulation using Contract Net Protocol (CNP) and Belief-State Inference.

## Project Overview

This repository contains the source code and evaluation experiments for the term project in the course **Intelligente Softwareagenten** (WS 2026/27) at the University of Rostock.

The goal of this project is to extend the classic "Hunt the Wumpus" environment into a Multi-Agent System (MAS). The following core concepts are planned and being integrated:

* **Communication & Protocols:** Contract Net Protocol (CNP) for decentralized task allocation (e.g., exploration, gold retrieval) using an auction-based mechanism.
* **Knowledge & Logic:** Belief-State Inference to model risk and uncertainty (pits, Wumpus) based on incomplete percepts (breeze, stench).
* **Visualization:** Interactive GUI (Tkinter) for real-time visualization of agent states, percepts, and auction dynamics.

## Requirements & Setup

### Prerequisites

* Python 3.10 or higher
* Standard library `tkinter` (on Linux systems, install via `sudo apt install python3-tk` if needed)

### Installation & Quickstart

1. Clone this repository:
   ```bash
   git clone https://github.com/astronerd21/multiagent-wumpus-world.git
   cd multiagent-wumpus-world
   ```

2. Run the main application (Interactive GUI):
   ```bash
   python main.py
   ```

## Authors & Group Members

* **astronerd21**, **MeisterBrowser**
* Course: *Intelligente Softwareagenten (23827)*
* Institution: University of Rostock

## AI Disclaimer & Policy Compliance (ACM Policy)

In accordance with the [ACM Publications Policies on AI Tools](https://www.acm.org/publications/policies/frequently-asked-questions), we disclose the use of generative AI technologies in this project:

* Generative AI tools (e.g., ChatGPT / Gemini) are utilized for initial brainstorming, drafting project documentation (such as repository setup and README files), and assistance during early prototyping.
* All generated content and prospective code implementations will be continuously verified, tested, and maintained by the team members.