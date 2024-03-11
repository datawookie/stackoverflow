export async function getServerSideProps(context) {
  const res = await fetch('http://backend:80');
  const pageContent = await res.text();
  return { props: { pageContent } };
}

function HomePage({ pageContent }) {
  return (
    <div>
      <h1>Welcome to My Next.js App</h1>
      {/* Print value of the NEXT_PUBLIC_BACKEND_BASE_URL environment variable. */}
      <p>API URL: {process.env.NEXT_PUBLIC_BACKEND_BASE_URL}</p>
      <hr></hr>
      {/* Include content from backend. */}
      <div dangerouslySetInnerHTML={{ __html: pageContent }} />
    </div>
  );
}

export default HomePage;
