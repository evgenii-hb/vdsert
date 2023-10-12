module.exports = {
    branches: [{name: 'main'}],
    plugins: [
        ["@semantic-release/commit-analyzer", {
            "preset": "angular",
            "releaseRules": [
                {type: 'feat', release: 'minor'},
                {type: 'fix', release: 'patch'},
                {type: 'perf', release: 'patch'},
                {type: 'docs', release: 'patch'},
                {type: 'refactor', release: 'patch'},
                {type: 'style', release: 'patch'},
                {type: 'ci', release: 'patch'},
                {type: 'chore', release: 'patch'}
            ]
        }],
        "@semantic-release/release-notes-generator",
        ["@semantic-release/github", {
            "assets": [
                {path: "dist/*"}
            ]
        }]
    ],
    verifyConditions: [
        "@semantic-release/github"
    ],
    prepare: [
    ],
    publish: [
        "@semantic-release/github"
    ],
};
