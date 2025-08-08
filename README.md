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

### **3. Social Media SoM**

* **Strategist Agent**:

  * Creates a **multi-platform promotion strategy** for X (Twitter), LinkedIn, and optionally Instagram.
* **Copywriter Agent**:

  * Writes **ready-to-publish** posts tailored to each platform, with hashtags and CTAs.
* **Campaign Approver (User Proxy)**:

  * Human reviewer to approve or suggest changes to social media copy.

### **4. Director (User Proxy)**

* Reviews **final article** and **social media posts** together.
* Provides final approval before publishing.

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

### **Strategist Agent**

* Role: Develop a social media promotion plan
* Platforms: X (Twitter), LinkedIn, Instagram
* Output: Platform-specific strategy document

### **Copywriter Agent**

* Role: Write social media posts
* Output: Platform-specific copy with hashtags and CTAs

### **Planner Agent**

* Role: Task orchestration and sequencing
* Output: JSON `{ "next_speaker": "<Agent>", "task_description": "<Instructions>" }`

### **Selector Agent**

* Role: Control conversation flow between Planner and teams

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


mention/edit task in main.py file and run:

python run main.py


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

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

