import { NextApiRequest, NextApiResponse } from "next";
import NextAuth from "next-auth";
import Providers from "next-auth/providers";
import getConfig from "next/config";
const { publicRuntimeConfig } = getConfig();

type Credentials = {
  adminName: string;
  password: string;
};

const adminCredentials = (credentials: Credentials) => {
  const adminName = process.env.ADMIN_NAME || "admin";
  const password = process.env.PASSWORD || "password";

  if (
    credentials.adminName === adminName &&
    credentials.password === password
  ) {
    return {
      name: "admin",
    };
  } else {
    return null;
  }
};

const options = {
  providers: [
    Providers.Credentials({
      name: "Admin",
      credentials: {
        adminName: { label: "Admin Name", type: "text", placeholder: "admin" },
        password: { label: "Password", type: "password" },
      },
      authorize: async (credentials: Credentials) => {
        const user = adminCredentials(credentials);

        if (user) {
          return Promise.resolve(user);
        }

        return Promise.resolve(null);
      },
    }),
  ],
  callbacks: {
    async redirect(props) {
      const { url, baseUrl } = props;
      const basePath = publicRuntimeConfig.basePath || "";

      return basePath;
    },
  },
};

export default (req: NextApiRequest, res: NextApiResponse) =>
  NextAuth(req, res, options);