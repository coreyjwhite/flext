import Link from "next/link";
import Heading from "components/Heading";

export default function Index() {
  return (
    <>
      <Heading>Hello, World!</Heading>
      <Link href="stylesheet" passHref>
        <a>Styles</a>
      </Link>
    </>
  );
}
