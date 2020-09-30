queries = [
    {
        "nome": "java",
        "query": """
query q {
  search(query: "stars:>10000 language:java", type: REPOSITORY, first: 100, after: %s) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
        languages(orderBy: {field: SIZE, direction: DESC}, first: 1) {
          totalSize
          totalCount
          edges {
            size
            node {
              name
            }
          }
        }
        stargazers {
          totalCount
        }
        url
        sshUrl
      }
    }
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
  }
}
        """
    },
    {
        "nome": "python",
        "query": """
        query q {
  search(query: "stars:>10000 language:python", type: REPOSITORY, first: 100, after: %s) {
    nodes {
      ... on Repository {
        nameWithOwner
        createdAt
        languages(orderBy: {field: SIZE, direction: DESC}, first: 1) {
          totalSize
          totalCount
          edges {
            size
            node {
              name
            }
          }
        }
        stargazers {
          totalCount
        }
        url
        sshUrl
      }
    }
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
  }
}
"""
    }
]
