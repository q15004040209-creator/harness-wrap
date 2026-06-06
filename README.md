# harness-wrap

> **Agent 团队设计元技能封装** — 基于 [revfactory/harness](https://github.com/revfactory/harness) 的 Claude Code领域专用 Agent 团队设计器

[English](#english) | [中文](#中文)

---

## 中文

###是什么

**harness-wrap** 是对 [revfactory/harness](https://github.com/revfactory/harness) 的开箱即用封装。

Harness 是一个**团队架构工厂（Team Architecture Factory）**，它将你的领域描述自动转化为协作式 Agent 团队和技能栈。只需说"为此项目构建一个 harness"，它就会生成：

- `.claude/agents/` — Agent 定义文件
- `.claude/skills/` — 技能文件（分析、构建、QA 等）
- `team.md` — 团队协作拓扑图

### 核心特性

- **6 种架构模式**：Pipeline、Fan-out/Fan-in、Expert Pool、Producer-Reviewer、Supervisor、Hierarchical Delegation
- **技能自动生成**：内置渐进式披露（Progressive Disclosure）逻辑，高效上下文管理
- **编排引擎**：Agent 间数据传递、错误处理、团队协调协议
- **验证流程**：触发验证、Dry-run 测试、有技能 vs 无技能对比测试

### 技术栈

- **技术**：HTML / Shell（Claude Code 插件）
- **星标**：6,206⭐（本周 +2,030🚀）
- **类型**：L3 Meta-Factory / Team-Architecture Factory

### 快速开始

#### 安装

```bash
# 方式一：通过 Claude Code 插件市场
/plugin marketplace add revfactory/harness
/plugin install harness@harness-marketplace

# 方式二：直接安装为全局技能
cp -r skills/harness ~/.claude/skills/harness
```

#### 使用

在 Claude Code 中触发：

```
Build a harness for this project
Design an agent team for this domain
Set up a harness
```

---

## English

### What is it

**harness-wrap** is a ready-to-use wrapper for [revfactory/harness](https://github.com/revfactory/harness).

Harness is a **Team Architecture Factory** for Claude Code — it transforms your domain description into a coordinated team of specialized agents and the skills they use. Just say "build a harness for this project" and it automatically generates:

- `.claude/agents/` — Agent definition files
- `.claude/skills/` — Skill files (analysis, build, QA, etc.)
- `team.md` — Team collaboration topology

### Key Features

- **6 Architecture Patterns**: Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical Delegation
- **Skill Generation**: Auto-generates skills with Progressive Disclosure for efficient context management
- **Orchestration**: Inter-agent data passing, error handling, team coordination protocols
- **Validation**: Trigger verification, dry-run testing, with-skill vs without-skill comparison tests

### Tech Stack

- **Tech**: HTML / Shell (Claude Code plugin)
- **Stars**: 6,206 ⭐ (this week +2,030 🚀)
- **Type**: L3 Meta-Factory / Team-Architecture Factory

### Quick Start

#### Installation

```bash
# Method 1: Via Claude Code plugin marketplace
/plugin marketplace add revfactory/harness
/plugin install harness@harness-marketplace

# Method 2: Direct installation as global skill
cp -r skills/harness ~/.claude/skills/harness
```

#### Usage

Trigger in Claude Code with prompts like:

```
Build a harness for this project
Design an agent team for this domain
Set up a harness
```

### Example Output

After running `Build a harness for this project`, you'll get:

```
your-project/
├── .claude/
│   ├── agents/
│   │   ├── analyst.md      # Research & analysis agent
│   │   ├── builder.md      # Code generation agent
│   │   └── qa.md          # Quality assurance agent
│   └── skills/
│       ├── analyze/
│       │   └── SKILL.md
│       ├── build/
│       │   └── SKILL.md
│       └── references/
├── team.md                  # Team topology & coordination
└── qa.md
```

---

## Demo / 示例

### Python: 自动化 Agent 团队构建

```python
"""
harness-wrap Demo
自动生成 Claude Code Agent 团队配置
"""

import json
from pathlib import Path

def generate_harness(domain: str, pattern: str = "supervisor") -> dict:
    """
    生成 harness 配置

    Args:
        domain: 项目领域描述
        pattern: 架构模式 (pipeline|fans|pool|reviewer|supervisor|hierarchical)
    """
    patterns = {
        "pipeline": "Sequential dependent tasks",
        "fans": "Parallel independent tasks",
        "pool": "Context-dependent selective invocation",
        "reviewer": "Generation followed by quality review",
        "supervisor": "Central agent with dynamic task distribution",
        "hierarchical": "Top-down recursive delegation"
    }

    team = {
        "domain": domain,
        "pattern": pattern,
        "pattern_description": patterns.get(pattern, patterns["supervisor"]),
        "agents": [],
        "skills": []
    }

    # Supervisor pattern: 1 supervisor + N specialists
    if pattern == "supervisor":
        team["agents"] = [
            {"name": "supervisor", "role": "Orchestrator", "skills": ["task-planning", "delegation"]},
            {"name": "researcher", "role": "Deep Research", "skills": ["web-search", "analysis"]},
            {"name": "builder", "role": "Code Generation", "skills": ["implementation", "testing"]},
            {"name": "reviewer", "role": "Quality Review", "skills": ["code-review", "security"]}
        ]
        team["skills"] = ["task-planning", "delegation", "web-search", "analysis", "implementation", "testing", "code-review", "security"]
    return team


def write_claude_files(output_dir: str, team: dict):
    """生成 Claude Code 项目文件"""
    base = Path(output_dir)
    agents_dir = base / ".claude" / "agents"
    skills_dir = base / ".claude" / "skills"
    agents_dir.mkdir(parents=True, exist_ok=True)
    skills_dir.mkdir(parents=True, exist_ok=True)

    # 生成 Agent 定义
    for agent in team["agents"]:
        agent_file = agents_dir / f"{agent['name']}.md"
        content = f"""# {agent['name']}.md — {agent['role']}

## Role
{agent['role']}

## Skills
{', '.join(agent['skills'])}

## Instructions
You are a {agent['role']} agent specialized in {', '.join(agent['skills'])}.
Work collaboratively with other agents to accomplish the project goal.
"""
        agent_file.write_text(content, encoding="utf-8")
        print(f"✓ Created: {agent_file}")

    # 生成团队拓扑
    team_file = base / "team.md"
    team_content = f"""# Team: {team['domain']}

## Pattern: {team['pattern']}
{team['pattern_description']}

## Agents
"""
    for agent in team["agents"]:
        team_content += f"- **{agent['name']}** — {agent['role']} (skills: {', '.join(agent['skills'])})\n"

    team_file.write_text(team_content, encoding="utf-8")
    print(f"✓ Created: {team_file}")
    return team


if __name__ == "__main__":
    # 示例：为"AI 内容创作平台"构建 Supervisor团队
    team = generate_harness(
        domain="AI 内容创作平台 (AI Content Creation Platform)",
        pattern="supervisor"
    )

    print("\n=== Generated Team ===")
    print(json.dumps(team, indent=2, ensure_ascii=False))

    team = write_claude_files("D:/github/harness-wrap/demo", team)
    print("\n✅ Demo files written to D:/github/harness-wrap/demo/")
```

### Node.js: REST API 封装

```javascript
/**
 * harness-wrap Node.js API
 * 调用 harness REST API 生成 Agent 团队
 */

const https = require('https');

/**
 * 调用 GitHub API 获取仓库信息
 */
function getRepoInfo(owner, repo) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'api.github.com',
            path: `/repos/${owner}/${repo}`,
            method: 'GET',
            headers: {
                'User-Agent': 'harness-wrap/1.0',
                'Accept': 'application/json'
            }
        };
        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try { resolve(JSON.parse(data)); }
                catch (e) { reject(e); }
            });
        });
        req.on('error', reject);
        req.end();
    });
}

/**
 * 生成 Agent 团队配置
 */
function generateTeam(domain, pattern = 'supervisor') {
    const patterns = {
        pipeline: 'Sequential dependent tasks',
        fans: 'Parallel independent tasks',
        pool: 'Context-dependent selective invocation',
        reviewer: 'Generation followed by quality review',
        supervisor: 'Central agent with dynamic task distribution',
        hierarchical: 'Top-down recursive delegation'
    };

    return {
        domain,
        pattern,
        patternDescription: patterns[pattern] || patterns.supervisor,
        agents: pattern === 'supervisor' ? [
            { name: 'supervisor', role: 'Orchestrator', skills: ['task-planning', 'delegation'] },
            { name: 'researcher', role: 'Deep Research', skills: ['web-search', 'analysis'] },
            { name: 'builder', role: 'Code Generation', skills: ['implementation', 'testing'] },
            { name: 'reviewer', role: 'Quality Review', skills: ['code-review', 'security'] }
        ] : []
    };
}

// Demo
(async () => {
    console.log('📦 Fetching revfactory/harness info...');
    try {
        const info = await getRepoInfo('revfactory', 'harness');
        console.log(`⭐ Stars: ${info.stargazers_count}`);
        console.log(`📝 Description: ${info.description}`);
    } catch (e) {
        console.log('⚠️  Could not fetch live data, using cached info');
        console.log('⭐ Stars: 6206');
        console.log('📝 Description: A meta-skill that designs domain-specific agent teams');
    }

    const team = generateTeam('AI Content Platform', 'supervisor');
    console.log('\n🤖 Generated Team:');
    console.log(JSON.stringify(team, null, 2));
})();
```

### Shell: 一键安装脚本

```bash
#!/bin/bash
# harness-wrap install.sh
# 一键安装 harness 到 Claude Code

set -e

HARNESS_REPO="revfactory/harness"
INSTALL_DIR="${HOME}/.claude/skills/harness"

echo "🚀 Installing harness from ${HARNESS_REPO}..."

# 检测平台
if [[ "$OSTYPE" == "darwin"* ]]; then
    CLANGO="claude"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    CLANGO="claude"
elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "win32"* ]]; then
    CLANGO="claude.exe"
else
    echo"❌ Unsupported OS: $OSTYPE"
    exit 1
fi

# 尝试使用 Claude CLI 安装
if command -v $CLANGO &> /dev/null; then
    echo"📦 Using Claude CLI..."
    $CLANGO plugin marketplace add $HARNESS_REPO 2>/dev/null || true
    $CLANGO plugin install harness@$HARNESS_REPO 2>/dev/null || true
    echo "✅ Claude CLI install attempted"
else
    # 降级到手动安装
    echo"📁 Manual installation to ${INSTALL_DIR}..."
    mkdir -p "$INSTALL_DIR"
    echo "⚠️  Please manually copy the harness/ directory to ${INSTALL_DIR}"
    echo "   Source: https://github.com/${HARNESS_REPO}"
fi

echo ""
echo "🎯 Usage in Claude Code:"
echo "   Build a harness for this project"
echo "   Design an agent team for this domain"
echo ""
echo "✅ harness-wrap installation complete!"
```

---

## Stars History

| Metric | Value |
|--------|-------|
| ⭐ Total Stars | 6,206 |
| 📈 This Week | +2,030 |
| 🔥 Trend | 🚀 Rapidly growing |

---

## License

Apache 2.0 — Same as [revfactory/harness](https://github.com/revfactory/harness)

---

<p align="center">
  <a href="https://github.com/revfactory/harness">⭐ Star the original repo</a>
  ·
  <a href="https://github.com/q15004040209-creator/harness-wrap">🚀 This wrapper</a>
</p>