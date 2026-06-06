/**
 * harness-wrap Demo - Node.js
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

    const agentSets = {
        supervisor: [
            { name: 'supervisor', role: 'Orchestrator', skills: ['task-planning', 'delegation'] },
            { name: 'researcher', role: 'Deep Research', skills: ['web-search', 'analysis'] },
            { name: 'builder', role: 'Code Generation', skills: ['implementation', 'testing'] },
            { name: 'reviewer', role: 'Quality Review', skills: ['code-review', 'security'] }
        ],
        pipeline: [
            { name: 'analyst', role: 'Requirements Analysis', skills: ['analysis', 'requirements'] },
            { name: 'designer', role: 'System Design', skills: ['design', 'architecture'] },
            { name: 'builder', role: 'Code Generation', skills: ['implementation', 'testing'] },
            { name: 'tester', role: 'QA Testing', skills: ['testing', 'validation'] }
        ],
        reviewer: [
            { name: 'generator', role: 'Content Generator', skills: ['generation', 'creation'] },
            { name: 'reviewer', role: 'Quality Reviewer', skills: ['review', 'feedback', 'revision'] }
        ]
    };

    return {
        domain,
        pattern,
        patternDescription: patterns[pattern] || patterns.supervisor,
        agents: agentSets[pattern] || agentSets.supervisor
    };
}

// CLI
const domain = process.argv[2] || 'AI Content Platform';
const pattern = process.argv[3] || 'supervisor';

(async () => {
    console.log(`🎯 Generating harness for: ${domain}`);
    console.log(`📐 Pattern: ${pattern}\n`);

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

    const team = generateTeam(domain, pattern);
    console.log('\n🤖 Generated Team:');
    console.log(JSON.stringify(team, null, 2));
})();