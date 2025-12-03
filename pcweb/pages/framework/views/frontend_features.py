import reflex as rx

from pcweb.pages.framework.components.stat import stat


def frontend_card(
    title: str,
    description: str,
    image: str,
    height: str = "auto",
    top: str = "5rem",
    cols: str = "1",
    image_cn: str = "",
) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.h2(title, class_name="font-large text-slate-12 z-[1]"),
            rx.el.p(description, class_name="font-base text-slate-9 z-[1] text-pretty"),
            class_name="flex flex-col gap-2 px-10 pt-10",
        ),
        rx.image(
            src=f"/landing/frontend_features/light/{image}",
            class_name="dark:hidden w-full absolute shrink-0" + " " + image_cn,
            top=top,
            height=height,
            loading="lazy",
            alt=title + " image",
        ),
        rx.image(
            src=f"/landing/frontend_features/dark/{image}",
            class_name="dark:block hidden w-full absolute shrink-0" + " " + image_cn,
            top=top,
            height=height,
            loading="lazy",
            alt=title + " image",
        ),
        class_name=f"lg:col-span-{cols} col-span-1 h-96 rounded-[1.125rem] bg-slate-2 border border-slate-3 overflow-hidden relative lg:shadow-large max-h-full pointer-events-none",
    )


def frontend_grid() -> rx.Component:
    return rx.box(
        frontend_card(
            title="Modular Security Framework",
            description="60+ integrated defense modules. Deploy threat intelligence, autonomous response, and predictive maintenance across your infrastructure.",
            image="components.svg",
            cols="2",
            height="17.5rem",
            top="6.5rem",
            image_cn="min-w-fit",
        ),
        frontend_card(
            title="Unified Operations Console",
            description="Real-time visibility across all assets. Monitor threats, manage incidents, and orchestrate unified response.",
            image="colors.svg",
            height="19.5rem",
            top="7rem",
        ),
        frontend_card(
            title="Context-Aware Dashboards",
            description="Adaptive interfaces for your environment. Custom views for SOC teams, threat hunters, compliance, and leadership.",
            image="ui.svg",
            height="17.5rem",
            top="6.5rem",
        ),
        frontend_card(
            title="Stealth Operations Mode",
            description="Combat-ready interface for continuous surveillance. Enhanced threat detection with zero visual fatigue.",
            image="dark_light_mode.svg",
            height="19.5rem",
            top="5rem",
        ),
        frontend_card(
            title="Deploy Anywhere",
            description="From corporate headquarters to remote facilities and tactical operations. Full security capabilities on any device, online or offline.",
            image="responsive.svg",
            height="19.5rem",
            top="5rem",
        ),
        frontend_card(
            title="Seamless Integration",
            description="Connect with your existing security stack, identity providers, SIEM platforms, and enterprise tools through native integrations and open APIs.",
            image="react.svg",
            cols="2",
            height="20rem",
            top="4rem",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-4 gap-4 grid-rows-2 max-w-[84.5rem]",
    )


def frontend_features() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                rx.el.h2(
                    "Architecture",
                    class_name="font-x-large text-slate-12 text-balance",
                ),
                rx.el.p(
                    "Built on Zero-Trust Architecture",
                    class_name="font-x-large text-slate-9 z-[1] text-balance",
                ),
                class_name="flex flex-col lg:border-r border-slate-3 lg:p-[5rem_6.5rem_5rem_2.5rem] lg:text-nowrap text-center lg:text-start pb-12 lg:pb-0 mt-12 lg:mt-0",
            ),
            rx.box(
                rx.el.p(
                    "Full-spectrum security from silicon to satellite. Every endpoint, every protocol, every threat surface secured with continuous verification and defense-in-depth architecture.",
                    class_name="font-base text-slate-11 text-pretty max-w-md",
                ),
                class_name="lg:px-10 lg:py-[5.5rem] py-12 w-auto border-b border-slate-3 lg:border-b-0",
            ),
            class_name="flex flex-col-reverse lg:flex-row lg:border-t border-slate-3 max-w-[64.19rem] justify-center lg:border-x w-full",
        ),
        frontend_grid(),
        rx.box(
            rx.box(
                rx.box(
                    rx.el.h3("Certified", class_name="font-smbold text-slate-9 text-sm"),
                    rx.el.p("SOC 2 Type II Certified", class_name="font-medium text-slate-12 text-base"),
                    class_name="flex flex-col gap-1 p-6 border border-slate-3 rounded-lg bg-slate-2",
                ),
                rx.box(
                    rx.el.h3("Compliant", class_name="font-smbold text-slate-9 text-sm"),
                    rx.el.p("ISO 27001 Compliant", class_name="font-medium text-slate-12 text-base"),
                    class_name="flex flex-col gap-1 p-6 border border-slate-3 rounded-lg bg-slate-2",
                ),
                rx.box(
                    rx.el.h3("Ready", class_name="font-smbold text-slate-9 text-sm"),
                    rx.el.p("FedRAMP Ready", class_name="font-medium text-slate-12 text-base"),
                    class_name="flex flex-col gap-1 p-6 border border-slate-3 rounded-lg bg-slate-2",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-[84.5rem] mt-8",
            ),
            class_name="w-full flex justify-center",
        ),
        class_name="flex flex-col justify-center items-center",
    )
