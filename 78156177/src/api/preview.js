const API_URL = process.env.WORDPRESS_API_URL

async function fetchAPI(query = "", { variables }) {
  const headers = { "Content-Type": "application/json" }

  if (process.env.WORDPRESS_AUTH_REFRESH_TOKEN) {
    headers["Authorization"] =
      `Bearer ${process.env.WORDPRESS_AUTH_REFRESH_TOKEN}`
  }

  // WPGraphQL Plugin must be enabled
  const res = await fetch(API_URL, {
    headers,
    method: "POST",
    body: JSON.stringify({
      query,
      variables,
    }),
  })

  const json = await res.json()

  if (json.errors) {
    console.error(json.errors)
    throw new Error("Failed to fetch API")
  }
  return json.data
}

export async function getPreviewPage(id, idType = "DATABASE_ID") {
  const data = await fetchAPI(
    `
    query PreviewPage($id: ID!, $idType: PageIdType!) {
      page(id: $id, idType: $idType) {
        databaseId
        slug
        title
        status
      }
    }`,
    {
      variables: { id, idType },
    },
  )
  return data?.page
}
