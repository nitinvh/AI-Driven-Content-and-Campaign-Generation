# AI Driven Content and Campaign Generation Tool

## 📌 Overview

The **AI Driven Content and Campaign Generation Tool** is an autonomous, multi-agent system designed to **create high-quality written content** and **generate targeted social media campaigns** with minimal human intervention.
It uses **Autogen** for orchestrating AI agents and **LangChain** for tool integration, with specialized agents working in a **round-robin workflow** to ensure quality and consistency.

The system supports:

* End-to-end **blog/article creation**
* Strategic **multi-platform social media promotion**
* **Human-in-the-loop approval** for final deliverables

---

## 🏗 Architecture

The project architecture follows a **Selector–Planner–Team** pattern:

 <img width="1759" height="660" alt="image" src="https://github.com/user-attachments/assets/2a69a998-400a-4416-911e-ab72143521f2" />


### **1. Selector Group Chat Team**

* **Selector Agent**: Controls the conversation flow between all agents based on the Planner’s JSON instructions.
* **Planner Agent**: Breaks high-level user goals into sequential tasks and assigns them to specialized teams.

### **2. Content Generation SoM (System of Machines)**

* **Researcher Agent**:

  * Gathers structured factual information using tools like **Tavily Search** and **Wikipedia Search**.
  * Outputs **markdown reports** with key points, supporting data, and sources.
* **Writer Agent**:

  * Converts research into a **complete draft article** with intro, body, and conclusion.
* **Editor Agent**:

  * Refines the draft for **clarity, grammar, tone, and flow**.
* **Content Reviewer (User Proxy)**:

  * Human reviewer who provides final feedback before moving to social media creation.
  * Termination Signal: APPROVED (from human)

### **3. Social Media SoM**

* **Strategist Agent**:

  * Creates a **multi-platform promotion strategy** for X (Twitter), LinkedIn, and optionally Instagram.
* **Copywriter Agent**:

  * Writes **ready-to-publish** posts tailored to each platform, with hashtags and CTAs.
* **Campaign Approver (User Proxy)**:

  * Human reviewer to approve or suggest changes to social media copy.
  * Termination Signal: APPROVED (from human)

### **4. Director (User Proxy)**

* Reviews **final article** and **social media posts** together.
* Provides final approval before publishing.
* Termination Signal: FINALIZE (from human)

---

## ⚙️ Tech Stack

| Component            | Technology Used                     |
| -------------------- | ----------------------------------- |
| Agent Orchestration  | Autogen                             |
| Tool Integration     | LangChain                           |
| Research Tools       | Tavily Search API, Wikipedia Search |
| Data Exchange Format | JSON, Markdown                      |
| Workflow Type        | Round Robin + Human-in-the-loop     |

---

## 🔄 Workflow

1. **User** gives a high-level goal to the **Planner Agent**.
2. **Planner Agent** assigns first task to **Content Generation SoM**.
3. **Content Generation SoM** agents execute in this order:
   `Researcher → Writer → Editor → Content Reviewer`
4. Once content is approved, **Planner Agent** assigns the task to **Social Media SoM**.
5. **Social Media SoM** agents execute in this order:
   `Strategist → Copywriter → Campaign Approver`
6. **Planner Agent** sends final outputs to **Human Director** for final approval.
7. If revisions are required, Planner reassigns tasks accordingly.

---

## 🤖 Agent Role Details

### **Researcher Agent**

* Role: Information gathering
* Tools: Tavily Search, Wikipedia Search (via LangChain)
* Output: Structured markdown report with:

  * **Key Points**
  * **Supporting Data**
  * **Key Sources**

### **Writer Agent**

* Role: Draft full article from research notes
* Style: Expert yet accessible tone
* Output: Complete blog/article draft

### **Editor Agent**

* Role: Refine clarity, grammar, flow, and tone
* Output: Polished final article for human review

### **Content Reviewer(UserProxy)**
* Gives feedbacks to Content Generation Team
* His/Her Approval is mandatory to pass to next team

### **Strategist Agent**

* Role: Develop a social media promotion plan
* Platforms: X (Twitter), LinkedIn, Instagram
* Output: Platform-specific strategy document

### **Copywriter Agent**

* Role: Write social media posts
* Output: Platform-specific copy with hashtags and CTAs

### **Campaign Approver(UserProxy)**
* Gives feedbacks to Social Media Team
* His/Her Approval is mandatory to pass to Human Director for review

### **Planner Agent**

* Role: Task orchestration and sequencing
* Output: JSON `{ "next_speaker": "<Agent>", "task_description": "<Instructions>" }`

### **Selector Agent**

* Role: Control conversation flow between Planner and teams

### **Human Director(UserProxy)**
* Gives feedbacks to both Teams
* His/Her Approval is mandatory to Finalize content

---

## 🧑‍💻 Setup & Installation

### **Prerequisites**

* Python 3.10+
* Tavily Search API key
* Autogen & LangChain installed
* Gemini Api Key/ Google Api Key

### **Installation**

```bash
git clone https://github.com/nitinvh/AI-Driven-Content-and-Campaign-Generation.git
cd ai-content-campaign-tool
pip install -r requirements.txt
```

### **Environment Variables**

Create `.env` file:

```env
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
```

---

## 🚀 Usage


### *Mention/edit task in main.py file in task section and run:*
```bash
python main.py
```
## 🔍 Example Flow

**User:**
"Create an article on sustainable energy trends in 2025 and prepare a social media campaign."

**Flow:**

1. Planner assigns to Content Generation SoM.
2. Researcher → Writer → Editor → Content Reviewer.
3. Planner assigns to Social Media SoM.
4. Strategist → Copywriter → Campaign Approver.
5. Final approval by Director.

---

## ✅ Features

* Modular **multi-agent system**
* Extensible to add more agents or platforms
* Human-in-the-loop quality control
* Integration with **external research tools**
* **Automatic workflow sequencing** via Selector and Planner

---

## Example Of Approved/Finalized Article and Campaign by Human Director:
**SUBJECT:** **Final Project Deliverables for "War 2 vs. Coolie" Content Initiative**

This project is now complete. All teams have successfully executed their tasks. I am pleased to present the two final deliverables for your review and approval:

1.  **The Final Article:** A detailed analysis of the competing blockbuster strategies of *War 2* and *Coolie*.
2.  **The Social Media Plan:** Approved promotional copy for X, LinkedIn, and Instagram.

---

### **Deliverable 1: Final Article**

## **Clash of Titans: War 2 vs. Coolie — An Analysis of Two Blockbuster Strategies**

### **Introduction: The Ultimate Box Office Showdown**

The Indian film industry is poised for a cinematic clash of monumental proportions. In one corner stands *War 2*, a powerhouse sequel from the established YRF Spy Universe, banking on franchise power and a colossal casting coup. In the other corner is *Coolie*, a cultural phenomenon in the making, driven by the potent combination of a legendary superstar and a visionary director. This article dissects the hype, business models, and box office potential of these two juggernauts to determine which strategy holds the edge in today's competitive landscape.

---

### **The Franchise Powerhouse: YRF's *War 2***

*War 2* represents the calculated, strategic approach to building a modern blockbuster. It relies on a proven formula, meticulously engineered for pan-Indian dominance.

**Sub-Heading: The Security of a Cinematic Universe**
As a cornerstone of the YRF Spy Universe, *War 2* doesn't start from scratch. It inherits a loyal fanbase, established lore, and the brand equity built by hits like *Ek Tha Tiger*, *War*, and *Pathaan*. This significantly de-risks the project, as audience familiarity and anticipation are already guaranteed.

**Sub-Heading: The North-South Casting Coup**
The masterstroke for *War 2* is its casting. Pitting two of India's most celebrated performers and dancers, Hrithik Roshan (representing Bollywood's sleekness) against Jr. NTR (representing Tollywood's raw intensity), is a move designed to unite audiences across the nation. This isn't just a face-off; it's a strategic business merger of star power.

**Sub-Heading: The Promise: A Globe-Trotting Spectacle**
The film promises a sleek, high-octane, globe-trotting spy thriller. Directed by Ayan Mukerji, the expectation is for cutting-edge action, stunning visuals, and a continuation of the high-stakes espionage that defines the YRF Spy Universe.

---

### **The Auteur-Star Phenomenon: *Coolie***

*Coolie* eschews the safety of a franchise for a different, arguably more volatile, kind of power: the explosive union of a cultural icon and a directorial visionary.

**Sub-Heading: The "Thalaivar" Factor**
Superstar Rajinikanth is not just an actor; he is a cultural institution. His name alone, especially in his home turf of Tamil Nadu, guarantees immense opening-day figures. *Coolie* leverages this unparalleled legacy, promising to present the 'Thalaivar' in a new, darker avatar that has fans buzzing.

**Sub-Heading: The Lokesh Kanagaraj Brand**
Director Lokesh Kanagaraj has become a brand unto himself. With a track record of creating raw, gritty, and interconnected gangster sagas (*Kaithi*, *Vikram*), his name now generates as much hype as his actors. His involvement promises a film that is dark, intense, and auteur-driven—a stark contrast to the polished feel of *War 2*.

**Sub-Heading: The Promise: A Raw, Unforgettable Force of Nature**
The combined force of Rajinikanth's screen presence and Kanagaraj's intense directorial style creates an "x-factor" that is difficult to quantify but impossible to ignore. The promise is not of a slick spy thriller, but of a raw, intense, and unforgettable cinematic experience.

---

### **Conclusion: Franchise Security vs. The "X-Factor"**

We are witnessing a fascinating case study in blockbuster strategy.
*   ***War 2*** bets on the security of its established universe and a calculated, pan-Indian casting strategy. It's the safe, powerful, and logical bet.
*   ***Coolie*** bets on the raw, lightning-in-a-bottle potential of a unique artistic union between a beloved star and a director at the peak of his powers. It's the bold, high-risk, high-reward play.

While *War 2* has the framework for guaranteed success, *Coolie* possesses the rare potential to transcend cinema and become a cultural event. The ultimate winner will be determined at the box office, but the battle for audience anticipation has already begun.

---

### **Deliverable 2: Approved Social Media Campaign**

The following copy has been finalized and approved for a coordinated promotional push across our key social channels.

**X (Twitter):**
> The ultimate box office battle is brewing! ⚔️
>
> In one corner: Hrithik Roshan & Jr. NTR's franchise giant, #War2.
> In the other: Rajinikanth & Lokesh Kanagaraj's cultural phenomenon, #Coolie.
>
> Which film carries the bigger hype? We break it down.
>
> Read the full analysis here: [LINK]
>
> #CoolieVsWar2 #IndianCinema #HrithikRoshan #JrNTR #Rajinikanth #Bollywood #Kollywood

**LinkedIn:**
> A fascinating case study in blockbuster strategy is unfolding in Indian cinema, pitting two distinct models against each other.
>
> 1️⃣ **The Franchise Model:** YRF's *War 2* leverages the immense power of its established Spy Universe, adding a monumental North-South casting collaboration with Hrithik Roshan and Jr. NTR. It's a calculated move to ensure pan-Indian dominance.
>
> 2️⃣ **The Director-Star Model:** *Coolie* relies on the explosive combination of a cultural icon, Superstar Rajinikanth, with a visionary director, Lokesh Kanagaraj, whose brand alone guarantees immense anticipation.
>
> Which strategy holds more weight in today's competitive market—the security of a cinematic universe or the raw potential of a unique artistic union? Our latest article analyzes the business, buzz, and box office potential of both juggernauts.
>
> Read the deep-dive analysis: [LINK]
>
> #FilmIndustry #BoxOffice #EntertainmentBusiness #MarketingStrategy #CinematicUniverse #War2 #Coolie #YRF #IndianCinema

**Instagram:**
> 🔥 CLASH OF TITANS! 🔥 The stage is set for one of the biggest cinematic showdowns in recent memory.
>
> Team #War2: The sleek, globe-trotting spy thriller from the YRF Spy Universe, featuring an epic face-off between two of India's best performers: Hrithik Roshan vs. Jr. NTR! 🌍💥
>
> Team #Coolie: A raw, intense force of nature pairing the legendary 'Thalaivar' Rajinikanth with the visionary director Lokesh Kanagaraj for a film that promises to be dark, gritty, and unforgettable. 👊🎬
>
> One has franchise power, the other has the "x-factor." Which movie are YOU betting on to become the next mega-blockbuster? Let us know in the comments! 👇
>
> For the full deep-dive analysis, hit the link in our bio!
>
> #CoolieVsWar2 #HrithikRoshan #JrNTR #Rajinikanth #Thalaivar #LokeshKanagaraj #AyanMukerji #YRFspyUniverse #Bollywood #Kollywood #IndianCinema #Movies #Film #ComingSoon

***

## **Note: Check supervised-content-creation-poc_op.txt file for detailed Output**

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

