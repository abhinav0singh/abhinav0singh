<img src="./assets/hero.svg" width="100%" alt="Abhinav Singh — Backend Engineer" />

<br>

<table>
<tr>
<td width="22%" align="center">
<img src="./assets/avatar.png" width="150" alt="Abhinav Singh" />
</td>
<td width="78%">

I'm a pre-final year IT student who likes backend systems — the kind of code where correctness under failure matters more than anything else. Two projects anchor most of what I do: **TitanServer**, a concurrent C++ server framework, and my **Banking Ledger**, a payments backend built around immutable double-entry records. Outside of that, I've dabbled in quant modelling, ML, and a fair amount of competitive programming.

🎓 Manipal Institute of Technology, Bengaluru — CGPA 8.52/10 &nbsp;·&nbsp; 🧑‍🏫 EducationLead, Quantus (Quantum Computing Club) &nbsp;·&nbsp; 📜 Certified in Data Analysis, HKUST &nbsp;·&nbsp; 🏆 300+ DSA, 100+ LeetCode

</td>
</tr>
</table>

![C++](https://img.shields.io/badge/C++-0A1120?style=flat-square&logo=cplusplus&logoColor=3DDCF0)
![JavaScript](https://img.shields.io/badge/JavaScript-0A1120?style=flat-square&logo=javascript&logoColor=56E39F)
![Python](https://img.shields.io/badge/Python-0A1120?style=flat-square&logo=python&logoColor=3DDCF0)
![SQL](https://img.shields.io/badge/SQL-0A1120?style=flat-square&logo=postgresql&logoColor=56E39F)
![Node.js](https://img.shields.io/badge/Node.js-0A1120?style=flat-square&logo=nodedotjs&logoColor=3DDCF0)
![MongoDB](https://img.shields.io/badge/MongoDB-0A1120?style=flat-square&logo=mongodb&logoColor=56E39F)
![Docker](https://img.shields.io/badge/Docker-0A1120?style=flat-square&logo=docker&logoColor=3DDCF0)
![Git](https://img.shields.io/badge/Git-0A1120?style=flat-square&logo=git&logoColor=56E39F)

---

### What I've built

<table>
<tr>
<td width="50%" valign="top">

**⚡ [TitanServer](https://github.com/abhinav0singh/TitanServer)**
Concurrent C++ server framework — `C++17` `std::thread` `CMake`

- Fixed a socket shutdown bug causing ~50% request failures; error rate to zero across 228k requests
- Diagnosed TIME_WAIT exhaustion, added keep-alive: **3,084 → 42,558 req/s (13.8×)**, p99 **6,691ms → 15ms**
- Traced a logging bottleneck to a mutex-guarded flush; gated it behind an atomic check for **11.5×** on static serving

</td>
<td width="50%" valign="top">

**🏦 [Banking Ledger](https://github.com/abhinav0singh/BankingTransactionSystem)**
RESTful payments backend — `Node.js` `Express` `MongoDB` `JWT`

- Modelled money as an **immutable double-entry ledger** — balances derived, never mutated, fully auditable
- **Idempotency keys** so a retried or duplicated request returns the original result, never a double-charge
- Multi-step transfers kept consistent with MongoDB sessions; JWT auth, bcrypt hashing, protected routes

</td>
</tr>
</table>

Also on GitHub: [Monte Carlo VaR/CVaR](https://github.com/abhinav0singh/Monte-Carlo_VaR_CVaR) · [Bangalore House Prices](https://github.com/abhinav0singh/Bangalore-house-Price-Prediction) · [java-visual-memory-trainer](https://github.com/abhinav0singh/java-visual-memory-trainer) · [→ all 31 repos](https://github.com/abhinav0singh?tab=repositories)

---

### Contributions

<img src="./assets/skyline.svg" width="100%" alt="A year of contributions, in 3D" />

---

<div align="center">

<a href="https://github.com/abhinav0singh"><img src="https://img.shields.io/badge/GitHub-0A1120?style=for-the-badge&logo=github&logoColor=56E39F" alt="GitHub" /></a>
<a href="https://www.linkedin.com/in/abhinav-singh-007-india/"><img src="https://img.shields.io/badge/LinkedIn-0A1120?style=for-the-badge&logo=linkedin&logoColor=3DDCF0" alt="LinkedIn" /></a>
<a href="https://leetcode.com/u/0eLVhF6Gzs/"><img src="https://img.shields.io/badge/LeetCode-0A1120?style=for-the-badge&logo=leetcode&logoColor=56E39F" alt="LeetCode" /></a>
<a href="mailto:abhinavsingh0176@gmail.com"><img src="https://img.shields.io/badge/Email-0A1120?style=for-the-badge&logo=gmail&logoColor=D7263D" alt="Email" /></a>

</div>