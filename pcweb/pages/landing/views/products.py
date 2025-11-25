import reflex as rx

from pcweb.components.icons.icons import get_icon
from pcweb.pages.docs import getting_started


def product_card(
    number: int,
    name: str,
    title: str,
    description: str,
    link: str,
    url: str,
    color: tuple[str, str],
    graphic: str,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(title, class_name="text-slate-12 text-xl font-semibold"),
            rx.el.span(description, class_name="text-slate-9 text-sm font-medium"),
            class_name="flex flex-col gap-2 px-10 pt-10",
        ),
        rx.el.div(
            rx.image(
                src=f"/landing/products/light/product_{graphic}.webp",
                class_name="w-auto pointer-events-none block dark:hidden",
            ),
            rx.image(
                src=f"/landing/products/dark/product_{graphic}.webp",
                class_name="w-auto pointer-events-none hidden dark:block",
            ),
            class_name="w-full max-h-[17.25rem] h-full overflow-hidden",
        ),
        rx.el.a(
            rx.el.span(
                link,
                class_name="text-sm font-medium text-slate-12 underline-none hover:text-slate-12",
            ),
            get_icon(
                "chevron_right",
                class_name="size-4 text-slate-9 group-hover:text-slate-12 group-hover:translate-x-1 transition-all duration-300",
            ),
            to=url,
            class_name="flex flex-row items-center gap-2 justify-between group h-[4rem] px-10 hover:bg-slate-2 transition-colors border-t max-lg:border-b border-slate-3",
        ),
        class_name="flex flex-col",
    )


def products() -> rx.Component:
    return rx.el.section(
        product_card(
            1,
            "AutoSecOps",
            "AutoSecOps Engine",
            "Self-healing security that detects, analyzes, and neutralizes threats in milliseconds—from edge sensors to orbital satellites—without human intervention.",
            "View Architecture",
            getting_started.introduction.path,
            ("violet", "9"),
            "ai",
        ),
        product_card(
            2,
            "Threat Intelligence",
            "Unified Threat Intelligence",
            "Global CTI feeds, Web Application Firewall, and Fraud Detection unified in one platform. Block APTs, fraud, and zero-days before impact.",
            "Explore Intelligence Suite",
            "/intelligence",
            ("jade", "10"),
            "framework",
        ),
        product_card(
            3,
            "Predictive Maintenance",
            "Predictive Maintenance & IoT Governance",
            "Monitor hardware health from silicon to chassis. ML-driven failure prediction, automated workflows, and device management for millions of endpoints.",
            "View Deployment Options",
            "/hosting",
            ("amber", "11"),
            "hosting",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3 lg:border-t",
    )
