from dataclasses import dataclass

import reflex as rx
import reflex_ui as ui

from pcweb.components.marquee import marquee


def get_highlight(text: str) -> rx.Component:
    return rx.el.span(text, class_name="text-primary-11")


def get_normal_text(*children) -> rx.Component:
    return rx.el.span(
        *children, class_name="text-secondary-12 text-sm font-medium text-wrap flex-1"
    )


@dataclass
class Social:
    name: str
    role: str
    text: str | rx.Component
    url: str | None = None
    avatar: str | None = None


SOCIALS_1 = [
    Social(
        name="Sarah Chen",
        role="Principal Security Engineer",
        text=get_normal_text(
            "We evaluated every major SIEM and XDR platform before choosing ",
            get_highlight("Singularity"),
            ". The AutoSecOps engine is the only system that actually delivers on the promise of autonomous threat response. Zero false positives in production.",
        ),
    ),
    Social(
        name="Marcus Rodriguez",
        role="CISO, Fortune 100 Manufacturer",
        text=get_normal_text(
            "After deploying ",
            get_highlight("Singularity"),
            " across 200,000 endpoints, our MTTD dropped from hours to seconds. The unified platform eliminated our entire integration layer—no more duct-taping tools together.",
        ),
        avatar="/landing/social/alex_opensea.webp",
    ),
    Social(
        name="James Liu",
        role="VP Infrastructure Security",
        text=get_normal_text(
            "Deployed ",
            get_highlight("Singularity"),
            " in our air-gapped defense network. Full stack visibility from firmware to cloud APIs. The predictive maintenance alone prevented $4M in potential downtime last quarter.",
        ),
    ),
]

SOCIALS_2 = [
    Social(
        name="Priya Sharma",
        role="Director of Security Operations",
        text=get_normal_text(
            "We're securing 15,000 IoT devices across six manufacturing plants with ",
            get_highlight("Singularity"),
            ". The edge-to-cloud visibility is unprecedented. Finally found a platform that actually understands OT/IT convergence.",
        ),
    ),
    Social(
        name="David Kowalski",
        role="Staff DevSecOps Engineer",
        text=get_normal_text(
            "This isn't hyperbole: ",
            get_highlight("Singularity"),
            " is the first security platform that integrates seamlessly into our CI/CD pipeline without slowing deployments. Security gates that actually make sense to engineers.",
        ),
    ),
    Social(
        name="Elena Volkov",
        role="Lead Security Architect",
        text=get_normal_text(
            "Evaluated the platform for our satellite operations—",
            get_highlight("Singularity"),
            " is the only system hardened for space-grade deployments. The zero-trust architecture works flawlessly in extreme latency environments.",
        ),
    ),
]


def social_card(social: Social) -> rx.Component:
    return rx.el.div(
        social.text,
        rx.el.div(
            ui.gradient_profile(
                seed=social.name,
                class_name="size-9 rounded-full",
            )
            if not social.avatar
            else rx.image(
                src=social.avatar,
                class_name="size-9 rounded-full",
            ),
            rx.el.div(
                rx.el.span(
                    social.name, class_name="text-secondary-12 font-medium text-sm"
                ),
                rx.el.span(
                    social.role, class_name="text-secondary-11 text-sm font-medium"
                ),
                class_name="flex flex-col",
            ),
            class_name="flex flex-row gap-4 mt-auto",
        ),
        rx.fragment(
            rx.el.a(
                to=social.url,
                target="_blank",
                class_name="absolute inset-0",
            ),
            ui.icon(
                "ArrowUpRight01Icon",
                class_name="group-hover:opacity-100 opacity-0 scale-50 group-hover:scale-100 transition-all duration-100 absolute bottom-4 right-4 size-5 text-primary-11 origin-bottom-left ease-in-out",
            ),
        )
        if social.url
        else None,
        class_name="flex flex-col gap-4 bg-slate-1 hover:bg-slate-2 transition-colors relative w-[22.5rem] h-[15rem] flex-shrink-0 p-6 group border-slate-4 py-10",
    )


def social_marquee() -> rx.Component:
    return rx.el.section(
        marquee(
            *[social_card(social) for social in SOCIALS_1],
            direction="left",
        ),
        marquee(
            *[social_card(social) for social in SOCIALS_2],
            direction="right",
        ),
        class_name="flex flex-col mx-auto w-full max-w-[64.19rem] lg:border-x justify-center items-center relative overflow-hidden border-slate-3 border-b",
    )
