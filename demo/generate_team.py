"""
harness-wrap Demo - Python
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
    elif pattern == "pipeline":
        team["agents"] = [
            {"name": "analyst", "role": "Requirements Analysis", "skills": ["analysis", "requirements"]},
            {"name": "designer", "role": "System Design", "skills": ["design", "architecture"]},
            {"name": "builder", "role": "Code Generation", "skills": ["implementation", "testing"]},
            {"name": "tester", "role": "QA Testing", "skills": ["testing", "validation"]}
        ]
        team["skills"] = ["analysis", "requirements", "design", "architecture", "implementation", "testing", "validation"]
    elif pattern == "reviewer":
        team["agents"] = [
            {"name": "generator", "role": "Content Generator", "skills": ["generation", "creation"]},
            {"name": "reviewer", "role": "Quality Reviewer", "skills": ["review", "feedback", "revision"]}
        ]
        team["skills"] = ["generation", "creation", "review", "feedback", "revision"]

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
    import sys

    # 默认：为"AI 内容创作平台"构建 Supervisor 团队
    domain = sys.argv[1] if len(sys.argv) > 1 else "AI 内容创作平台 (AI Content Creation Platform)"
    pattern = sys.argv[2] if len(sys.argv) > 2 else "supervisor"

    print(f"🎯 Generating harness for: {domain}")
   print(f"📐 Pattern: {pattern}\n")

    team = generate_harness(domain=domain, pattern=pattern)

    print("=== Generated Team ===")
    print(json.dumps(team, indent=2, ensure_ascii=False))

    output_dir = Path(__file__).parent
    team = write_claude_files(str(output_dir), team)
    print(f"\n✅ Demo files written to {output_dir}/")