import * as React from "react"
import { getPreviewPage } from "@api/preview"

const Preview = ({ serverData }) => (
  <main>
    <h1>SSR page</h1>
    <h2>Page title: {serverData.title}</h2>
  </main>
)

export default Preview

export async function getServerData({ query }) {
  const page = await getPreviewPage(query.id)

  return {
    props: page,
  }
}
