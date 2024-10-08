"use client";

// Components
import { Button } from "@/components/ui/button";

// Contexts
import { AuthContext } from "@/contexts/AuthContext";

// Next
import Image from "next/image";

// React
import { useCallback, useContext } from "react";

const LoginPage = () => {
  const { login } = useContext(AuthContext);

  const handleSignIn = useCallback(async () => {
    await login();
  }, [login]);

  return (
    <div className="flex flex-col gap-16 items-center h-full justify-center">
      <div>
        <div className=" text-2xl font-bold flex flex-col gap-1">
          <p>K-Dorm</p>
          <p>ระบบจัดการหอพักนักศึกษาอัจฉริยะ</p>
        </div>

        <p className="mt-4">
          แอปพลิเคชั่นจัดการหอพักสำหรับนักศึกษา สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
        </p>
      </div>

      <div className="flex flex-col items-center justify-center gap-16 w-full">
        <Image src="/assets/login/login.webp" width={325} height={325} alt="Login Logo" />

        <Button className="w-full font-bold rounded-xl" onClick={handleSignIn}>
          เข้าสู่ระบบโดยใช้ Google Account
        </Button>
      </div>
    </div>
  );
};

export default LoginPage;
