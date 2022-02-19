import SwaggerUI from "swagger-ui-react";
import "swagger-ui-react/swagger-ui.css";
import useApiUrl from "libs/useApiUrl";

export default function ApiSpec() {
  return <SwaggerUI url="http://192.168.1.77:5000/openapi" />;
}
