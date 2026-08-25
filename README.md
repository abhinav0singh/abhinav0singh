<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:312E81,100:6D28D9&height=230&section=header&text=Hi%2C%20I%27m%20Abhinav%20%F0%9F%91%8B&fontSize=42&fontColor=F8FAFC&fontAlignY=36&desc=Backend%20Engineer%20who%20obsesses%20over%20what%20happens%20when%20things%20fail&descAlignY=58&descSize=16&animation=fadeIn" width="100%"/>

<a href="https://github.com/abhinav0singh">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=20&duration=3200&pause=900&color=A78BFA&center=true&vCenter=true&width=760&lines=Concurrent+systems+%7C+Distributed+backends;13.8x+throughput%2C+one+keep-alive+header+at+a+time;Modelling+money+as+an+immutable+ledger;Probably+staring+at+a+p99+graph+right+now" alt="Typing SVG" />
</a>

</div>

<br/>

## `$ whoami`

<table>
<tr>
<td width="150" valign="top" align="center">
  <img src="assets/avatar.png" width="130" alt="Abhinav Singh"/>
</td>
<td valign="top">

<pre>
abhinav@backend:~$ cat about.md

Pre-final year IT student who cares more about what happens
when things go wrong than when they go right.

Two projects anchor most of what I do:
  → TitanServer      concurrent C++ server framework
  → Banking Ledger    payments backend, immutable double-entry ledger

Also spend time on quant modelling, ML, and competitive programming.
</pre>

🎓&nbsp;&nbsp;Manipal Institute of Technology, Bengaluru — CGPA 8.52/10<br/>
🧑‍🏫&nbsp;&nbsp;Education Lead, Quantus (Quantum Computing Club)<br/>
📜&nbsp;&nbsp;Certified in Data Analysis, HKUST<br/>
🏆&nbsp;&nbsp;300+ DSA problems solved · 100+ on LeetCode

</td>
</tr>
</table>

---

## `$ tech --stack`

**Languages**
<br/>
![C++](https://img.shields.io/badge/C%2B%2B-0B1120?style=flat-square&logo=cplusplus&logoColor=00599C)
![JavaScript](https://img.shields.io/badge/JavaScript-0B1120?style=flat-square&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/Python-0B1120?style=flat-square&logo=python&logoColor=3776AB)
![SQL](https://img.shields.io/badge/SQL-0B1120?style=flat-square&logo=postgresql&logoColor=4169E1)

**Backend & Runtime**
<br/>
![Node.js](https://img.shields.io/badge/Node.js-0B1120?style=flat-square&logo=nodedotjs&logoColor=339933)
![Express](https://img.shields.io/badge/Express-0B1120?style=flat-square&logo=express&logoColor=FFFFFF)
![CMake](https://img.shields.io/badge/CMake-0B1120?style=flat-square&logo=cmake&logoColor=064F8C)

**Data & Infra**
<br/>
![MongoDB](https://img.shields.io/badge/MongoDB-0B1120?style=flat-square&logo=mongodb&logoColor=47A248)
![Docker](https://img.shields.io/badge/Docker-0B1120?style=flat-square&logo=docker&logoColor=2496ED)
![Git](https://img.shields.io/badge/Git-0B1120?style=flat-square&logo=git&logoColor=F05032)
![Linux](https://img.shields.io/badge/Linux-0B1120?style=flat-square&logo=linux&logoColor=FCC624)

---

## 🚀 Featured builds

### ⚡ [TitanServer](https://github.com/abhinav0singh/TitanServer)
Concurrent C++ server framework — `C++17` `std::thread` `CMake`

- Fixed a socket shutdown bug causing ~50% request failures — error rate to zero across 228k requests
- Diagnosed TIME_WAIT exhaustion, added keep-alive: **3,084 → 42,558 req/s (13.8×)**, p99 **6,691ms → 15ms**
- Traced a logging bottleneck to a mutex-guarded flush; gated it behind an atomic check for **11.5×** on static serving

### 🏦 [Banking Ledger](https://github.com/abhinav0singh/BankingTransactionSystem)
RESTful payments backend — `Node.js` `Express` `MongoDB` `JWT`

- Modelled money as an **immutable double-entry ledger** — balances derived, never mutated, fully auditable
- **Idempotency keys** so a retried or duplicated request returns the original result, never a double-charge
- Multi-step transfers kept consistent with MongoDB sessions; JWT auth, bcrypt hashing, protected routes

Also shipped: [Monte Carlo VaR/CVaR](https://github.com/abhinav0singh/Monte-Carlo_VaR_CVaR) · [Bangalore House Price Prediction](https://github.com/abhinav0singh/Bangalore-house-Price-Prediction) · [java-visual-memory-trainer](https://github.com/abhinav0singh/java-visual-memory-trainer) · [→ browse all 31 repos](https://github.com/abhinav0singh?tab=repositories)

---

## 📊 By the numbers

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=abhinav0singh&show_icons=true&theme=tokyonight&hide_border=true&count_private=true"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=abhinav0singh&layout=compact&theme=tokyonight&hide_border=true"/>

<img src="https://streak-stats.demolab.com/?user=abhinav0singh&theme=tokyonight&hide_border=true"/>

<img src="https://github-profile-trophy.vercel.app/?username=abhinav0singh&theme=tokyonight&no-frame=true&row=1&column=6"/>

</div>

---

## 🐍 Contribution snake

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/abhinav0singh/abhinav0singh/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/abhinav0singh/abhinav0singh/output/github-contribution-grid-snake.svg" />
  <img alt="a snake eating the contribution graph" src="https://raw.githubusercontent.com/abhinav0singh/abhinav0singh/output/github-contribution-grid-snake.svg" width="100%"/>
</picture>

<sub>Rebuilt daily by <a href=".github/workflows/snake.yml">.github/workflows/snake.yml</a> — the image appears after the workflow runs once (see setup notes below).</sub>

---

## 🌆 A year in contributions

<div align="center">
<img src="assets/skyline.svg" width="100%" alt="3D contribution skyline"/>
</div>

---

## 🤝 Let's connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abhinav0singh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhinav-singh-007-india/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/0eLVhF6Gzs/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abhinavsingh0176@gmail.com)

![Profile views](https://komarev.com/ghpvc/?username=abhinav0singh&color=6d28d9&style=flat-square&label=Profile+views)

</div>

<details>
<summary>⚙️ How this README stays alive</summary>
<br/>

Nothing here is a hand-edited static image. The pieces that update on their own:

- **Stats · streak · top languages · trophies** — rendered on request by `github-readme-stats`, `github-readme-streak-stats`, and `github-profile-trophy`. No setup needed, they just read the public profile.
- **Contribution snake** — a scheduled GitHub Action (`Platane/snk`) rebuilds it daily and pushes the SVGs to an `output` branch.
- **3D skyline** — regenerated by its own existing workflow from the contribution calendar.
- **Header / typing line** — `capsule-render` and `readme-typing-svg`, both stateless SVG generators, no GitHub API calls involved.

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:312E81,100:6D28D9&height=110&section=footer" width="100%"/>
</div>
