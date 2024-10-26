"use client";

// Components
import StaffLeftMenu from "@/components/StaffLeftMenu";
import StaffRightMenu from "@/components/StaffRightMenu";
import { Toaster } from "@/components/ui/toaster";

// Next
import { usePathname } from "next/navigation";

// React
import { ReactNode, useEffect, useState } from "react";

const StaffLayout = ({
  children,
}: Readonly<{
  children: ReactNode;
}>) => {
  const pathname = usePathname();
  const [shouldShowMenu, setShouldShowMenu] = useState(false);

  useEffect(() => {
    setShouldShowMenu(pathname !== "/staff/login");
  }, [pathname]);

  return (
    <main className={"h-[100dvh] overflow-y-scroll"}>
      <div className="h-full flex flex-row">
        {shouldShowMenu && (
          <div className="min-w-64 h-full">
            <StaffLeftMenu />
          </div>
        )}

        <div className="w-full max-h-[100dvh] overflow-auto">
          {children}
          <Toaster />
        </div>

        {shouldShowMenu && (
          <div className="w-[3.5%] h-full">
            <StaffRightMenu />
          </div>
        )}
      </div>
    </main>
  );
};

export default StaffLayout;
